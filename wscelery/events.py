import logging
import threading
import time

from cachetools import LRUCache
from celery.events import EventReceiver
import tornado.gen
from tornado.ioloop import PeriodicCallback
from tornado.queues import Queue

logger = logging.getLogger(__name__)


class EventMonitor(threading.Thread):
    max_events = 100

    def __init__(self, capp, io_loop):
        """Monitors and stores events received from celery."""
        super().__init__()
        self.capp = capp
        self.io_loop = io_loop
        self.events = Queue(self.max_events)

    def run(self):
        # We don't want too frequent retries
        try_interval = 1
        while True:
            try:
                try_interval *= 2

                with self.capp.connection() as conn:
                    recv = EventReceiver(conn,
                                         handlers={'*': self.on_event},
                                         app=self.capp)
                    try_interval = 1
                    recv.capture(limit=None, timeout=None, wakeup=True)
            except (KeyboardInterrupt, SystemExit):
                import _thread
                _thread.interrupt_main()
            except Exception as e:
                logger.error('Failed to capture events: "%s", '
                             'trying again in %s seconds.',
                             e, try_interval)
                logger.debug(e, exc_info=True)
                time.sleep(try_interval)

    def on_event(self, event):
        """Called when an event from celery is received."""
        # Transfer control to IOLoop, tornado.queue is not thread-safe
        self.io_loop.add_callback(self.events.put, event)


class EventHandler:
    events_enable_interval = 5000  # in seconds
    # Maximum number of finished items to keep track of
    max_finished_history = 1000
    # celery events that represent a task finishing
    finished_events = (
        'task-succeeded',
        'task-failed',
        'task-rejected',
        'task-revoked',
    )

    def __init__(self, capp, io_loop):
        """Monitors events that are received from celery.

        capp - The celery app
        io_loop - The event loop to use for dispatch
        """
        super().__init__()

        self.capp = capp
        self.timer = PeriodicCallback(self.on_enable_events,
                                      self.events_enable_interval)

        self.monitor = EventMonitor(self.capp, io_loop)
        self.listeners = {}
        self.finished_tasks = LRUCache(self.max_finished_history)

    @tornado.gen.coroutine
    def start(self):
        """Start event handler.

        Expects to be run as a coroutine.
        """
        self.timer.start()
        logger.debug('Starting celery monitor thread')
        self.monitor.start()

        while True:
            event = yield self.monitor.events.get()
            try:
                task_id = event['uuid']
            except KeyError:
                continue

            try:
                callback = self.listeners[task_id]
            except KeyError:
                pass
            else:
                # Record finished tasks in-case they are requested
                # too late or are re-requested.
                if event['type'] in self.finished_events:
                    self.finished_tasks[task_id] = event
                callback(event)

    def stop(self):
        self.timer.stop()
        # FIXME: can not be stopped gracefully
        # self.monitor.stop()

    def on_enable_events(self):
        """Called periodically to enable events for workers
        launched after the monitor.
        """
        try:
            self.capp.control.enable_events()
        except Exception as e:
            logger.debug('Failed to enable events: %s', e)

    def add_listener(self, task_id, callback):
        """Add event listener for a task with ID `task_id`."""
        try:
            event = self.finished_tasks[task_id]
        except KeyError:
            self.listeners[task_id] = callback
        else:
            # Task has already finished
            callback(event)

    def remove_listener(self, task_id):
        """Remove listener for `task_id`."""
        try:
            del self.listeners[task_id]
        except KeyError:  # may have been cached
            pass
