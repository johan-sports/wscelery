#!/usr/bin/env python3

import logging

import tornado.websocket

from wscelery.utils import exclude_keys

logger = logging.getLogger(__name__)


def parse_event(event):
    return exclude_keys(event, (
        'hostname',
        'pid',
        'queue',
        'exchange',
    ))


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def initialize(self, events):
        self.task_id = None
        self.events = events

    # Allow any origin for now
    # FIXME: Security concern
    def check_origin(self, origin):
        return True

    def _handle_event(self, event):
        self.write_message(parse_event(event))

    def open(self):
        self.task_id = self.get_argument('id')
        self.events.add_listener(self.task_id, self._handle_event)

    def on_message(self):
        # Ignore any messages for now. This could be a better way
        # to request task status.
        pass

    def on_close(self):
        if self.task_id:
            self.events.remove_listener(self.task_id)
