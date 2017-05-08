#!/usr/bin/env python3

import json
import logging

import tornado.websocket

logger = logging.getLogger(__name__)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def initialize(self, events):
        self.events = events
        self.closed = True

    # Allow any origin for now
    # FIXME: Security concern
    def check_origin(self, origin):
        return True

    def _handle_event(self, event):
        if not self.closed:
            self.write_message(json.dumps(event))

    def open(self):
        self.closed = False
        # TODO: Make this a URL param
        self.task_id = self.get_argument('id')
        self.events.add_listener(self.task_id, self._handle_event)

    def on_message(self):
        # Ignore any messages for now. This could be a better way
        # to request task status.
        pass

    def on_close(self):
        self.closed = True
        self.events.remove_listener(self.task_id)
