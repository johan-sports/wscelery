from tornado.web import url

from wscelery.websocket import WebSocketHandler


def make_handlers(events):
    return [
        url(r'/', WebSocketHandler, dict(events=events)),
    ]
