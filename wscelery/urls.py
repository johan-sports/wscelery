from tornado.web import url

from wscelery.websocket import WebSocketHandler


def make_handlers(events, options):
    return [
        url(r'/(?P<task_id>[\w\-]+)', WebSocketHandler, {
            'events': events,
            'allow_origin': options.allow_origin,
        }),
    ]
