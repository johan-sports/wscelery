import atexit
import logging
import os
import re
import signal
import sys

from celery.bin.base import Command
from tornado.log import enable_pretty_logging
from tornado.options import options, parse_command_line

from wscelery.app import WsCelery
from wscelery.options import default_options

logger = logging.getLogger(__name__)


class WsCeleryCommand(Command):
    ENV_VAR_PREFIX = 'WSCELERY_'

    def run_from_argv(self, prog_name, argv=None, **kwargs):
        self.apply_env_options()
        self.apply_options(prog_name, argv)
        self.validate_options()

        self.setup_logging()

        wscelery = WsCelery(capp=self.app, options=options or default_options)
        # Graceful exit
        atexit.register(wscelery.stop)

        def sigterm_handler(signal, frame):
            logger.info('SIGTERM detected, shutting down')
            sys.exit(0)
        signal.signal(signal.SIGTERM, sigterm_handler)

        try:
            wscelery.start()
        except (KeyboardInterrupt, SystemExit):
            pass

    def handle_argv(self, prog_name, argv=None):
        self.run_from_argv(prog_name, argv)

    def apply_env_options(self):
        """Apply options passed through environment variables."""
        env_options = filter(self.is_app_envvar, os.environ)
        for env_var_name in env_options:
            name = env_var_name.replace(self.ENV_VAR_PREFIX, '', 1).lower()
            value = os.environ[env_var_name]
            try:
                option = options._options[name]
            except KeyError:
                option = options._options[name.replace('_', '-')]
            if option.multiple:
                value = [option.type(i) for i in value.split(',')]
            else:
                value = option.type(value)
            setattr(options, name, value)

    def apply_options(self, prog_name, argv):
        argv = list(filter(self.is_app_option, argv))
        parse_command_line([prog_name] + argv)

    def validate_options(self):
        origin = options.allow_origin
        if origin is not None:
            try:
                re.compile(origin)
            except Exception:
                msg = 'Invalid `allow_origin` regex r"{}"'
                raise Command.UsageError(msg.format(origin))

    def setup_logging(self):
        if options.debug and options.logging == 'info':
            options.logging = 'debug'
            enable_pretty_logging()
        else:
            logging.getLogger('tornado.access').addHandler(
                logging.NullHandler())
            logging.getLogger('tornado.access').propagate = False

    @staticmethod
    def is_app_option(arg):
        name, _, value = arg.lstrip('-').partition('=')
        name = name.replace('-', '_')
        return hasattr(options, name)

    def is_app_envvar(self, name):
        return name.startswith(self.ENV_VAR_PREFIX) and \
            name[len(self.ENV_VAR_PREFIX):].lower() in default_options
