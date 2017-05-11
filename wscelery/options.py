from tornado.options import define, options


define('port', default=1337,
       help='run on the given port', type=int)
define('address', default='',
       help='run on given address', type=str)
define('debug', default=False,
       help='run in debug mode', type=bool)
define('allow_origin', default=None,
       help='regex for allowed origins')

# TODO: Support SSL certs

default_options = options
