from config import Config
import logging

class Logger(object):

    """
    Wrapper class on logging
    """

    @classmethod
    def get_logger(cls, name):
        _logger = logging.getLogger(name)
        _logger.addHandler(logging.StreamHandler())

        debug_enabled = Config.get('logging', 'info') == 'debug'

        if debug_enabled == True:
            _logger.setLevel(logging.DEBUG)
        else:
            _logger.setLevel(logging.INFO)
        return _logger
