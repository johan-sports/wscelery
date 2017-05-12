from unittest import mock

from celery.bin.base import Command
from tornado.options import options

from wscelery.tests import AsyncHTTPTestCase
from wscelery.command import WsCeleryCommand


class OptionsTestCase(AsyncHTTPTestCase):
    def mock_option(self, name, value):
        return mock.patch.object(options.mockable(), name, value)


class TestWsCeleryCommand(OptionsTestCase):
    def test_port(self):
        with self.mock_option('port', 1337):
            command = WsCeleryCommand()
            command.apply_options('wscelery', argv=['--port=4321'])
            self.assertEqual(options.port, 4321)

    def test_address(self):
        with self.mock_option('address', '127.0.0.1'):
            command = WsCeleryCommand()
            command.apply_options('wscelery', argv=['--address=foobar'])
            self.assertEqual(options.address, 'foobar')

    def test_allow_origin_regex(self):
        with self.mock_option('allow_origin', None):
            command = WsCeleryCommand()
            command.apply_options('wscelery', argv=['--allow-origin=.*'])
            self.assertEqual(options.allow_origin, '.*')

    def test_invalid_allow_origin_regex(self):
        with self.mock_option('allow_origin', None):
            command = WsCeleryCommand()
            command.apply_options('wscelery', argv=['--allow-origin=*'])
            try:
                command.execute_from_commandline()
            except Command.UsageError:
                pass
            else:
                self.fail('Expected invalid regex to fail')
