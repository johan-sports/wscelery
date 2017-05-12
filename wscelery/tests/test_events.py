from unittest import mock

from tornado.testing import AsyncTestCase, gen_test

from wscelery.events import EventHandler


class EventHandlerTest(AsyncTestCase):
    def setUp(self):
        self.capp = mock.Mock()
        self.events = EventHandler(self.capp, self.io_loop)

    @gen_test
    def test_calls_callback_on_event_with_uuid(self):
        pass
