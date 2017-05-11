#!/usr/bin/env python3

import logging
import re

import tornado.websocket

from wscelery.utils import exclude_keys

logger = logging.getLogger(__name__)


def parse_event(event):
    return exclude_keys(event, (
        'hostname',
        'pid',
        'queue',
        'exchange',
        'args',
        'kwargs',
    ))


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def initialize(self, events, allow_origin=None):
        self.task_id = None
        self.events = events
        self.allow_origin = allow_origin

    def check_origin(self, origin):
        if not self.allow_origin:
            return super().check_origin(origin)
        match = re.match(self.allow_origin, origin)
        return match is not None

    def _handle_event(self, event):
        self.write_message(parse_event(event))

    def open(self, task_id):
        self.task_id = task_id
        self.events.add_listener(self.task_id, self._handle_event)

    def on_message(self):
        # Ignore any messages for now. This could be a better way
        # to request task status.
        pass

    def on_close(self):
        if self.task_id:
            self.events.remove_listener(self.task_id)
