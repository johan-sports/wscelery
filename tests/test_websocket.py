from tornado import gen
from tornado.websocket import websocket_connect
from tornado.testing import AsyncHTTPTestCase


class WebSocketTestCase(AsyncHTTPTestCase):
    @gen.coroutine
    def ws_connect(self, path, **kwargs):
        ws = yield websocket_connect(
            'ws://127.0.0.1:%d%s' % (self.get_http_port(), path),
            **kwargs
        )
        raise gen.Return(ws)

    @gen.coroutine
    def close(self, ws):
        ws.close()
        yield self.close_future
