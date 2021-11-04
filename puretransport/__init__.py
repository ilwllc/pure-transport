import traceback

__version__ = '0.2.1.ILW'

try:
    from .factory import transport_factory
except ImportError as ex:
    print(f'{ex.args[0]}')
    print(''.join(traceback.TracebackException.from_exception(ex).format()))
