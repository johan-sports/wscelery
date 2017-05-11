import unittest

from tornado.ioloop import IOLoop

from wscelery.events import EventHandler


class EventHandlerTest(unittest.TestCase):
    def setUp(self):
        self.io_loop = IOLoop.instance()
        self.events = EventHandler(capp=self.capp,
                                   io_loop=self.io_loop)
