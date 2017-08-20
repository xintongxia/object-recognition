import constants
import yaml

class Config(object):
    """
    A class to read config/config.yaml
    """
    with open ('config/config.yaml', 'r') as stream:
        _config = yaml.load(stream)

    @classmethod
    def get(cls, name, default=None):
        return cls._config.get(name, default)

    @classmethod
    def set_mode(cls, mode):
        if mode not in constants.MODES:
            raise Exception('Unsupported mode')
        cls._config['mode'] = mode
