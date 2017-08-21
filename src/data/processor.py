from src.utils import Config
import os

class Processor(object):

    dataset_conf = Config.get('datasets')

    @classmethod
    def download(cls, name):
        for conf in cls.dataset_conf:
            if conf.get('name') == name:
                cls._download(name, conf.get('url'))
                return

        raise Exception('Data set {} not found in base.yaml'.format(name))

    @classmethod
    def get_raw_dataset_dir(cls, name):
        return '{}/raw/{}'.format(Config.get('data_raw_dir'), name)

    @classmethod
    def _download(cls, name, url):
        dataset_dir = cls.get_raw_dataset_dir(name)
        os.system('mkdir -p {}'.format(dataset_dir))
        os.system('wget {} -P {}'.format(url, dataset_dir))
