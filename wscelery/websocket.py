#!/usr/bin/env python3

import json
import logging

import tornado.websocket

from wscelery.utils import select_keys

logger = logging.getLogger(__name__)


def parse_event(event):
    default_keys = ['uuid', 'timestamp']
    if event['type'] == 'task-successful':
        return select_keys(event, default_keys + ['result'])
    elif event['type'] == 'task-failed':
        return event
    return select_keys(event, default_keys)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def initialize(self, events):
        self.events = events

    # Allow any origin for now
    # FIXME: Security concern
    def check_origin(self, origin):
        return True

    def _handle_event(self, event):
        client_event = parse_event(event)
        self.write_message(json.dumps(client_event))

    def open(self):
        self.task_id = self.get_argument('task_id')
        self.events.add_listener(self.task_id, self._handle_event)

    def on_message(self):
        # Ignore any messages for now. This could be a better way
        # to request task status.
        pass

    def on_close(self):
        self.events.remove_listener(self.task_id)
