import yaml

class Config(object):
    """
    A class to read configs (config/base.yaml and config/config.yaml)
    """
    _config = {}
    with open ('config/base.yaml', 'r') as stream:
        _config.update(yaml.load(stream))
    with open ('config/config.yaml', 'r') as stream:
        _config.update(yaml.load(stream))

    @classmethod
    def get(cls, name, default=None):
        return cls._config.get(name, default)
