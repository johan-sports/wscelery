import celery
import tornado.testing
from tornado.options import options

from wscelery.app import WsCelery
from wscelery.options import default_options


class AsyncHTTPTestCase(tornado.testing.AsyncHTTPTestCase):
    """Default HTTP test case for WSCelery."""
    def get_app(self):
        capp = celery.Celery()
        return WsCelery(capp=capp, options=options or default_options)
