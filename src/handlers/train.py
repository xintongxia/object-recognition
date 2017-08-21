from src.data import Processor
from src.utils import Config, Logger
import urllib

logger = Logger.get_logger('TrainHandler')

class TrainHandler(object):

    train_sets = Config.get('train').get('train_sets', [])
    test_sets = Config.get('train').get('test_sets', [])

    @classmethod
    def handle(cls):
        cls._download_data()
        cls._convert_data()
        cls._split_data()
        cls._train()

    @classmethod
    def _download_data(cls):
        logger.debug('Fetching data sets: ' + str(cls.train_sets))
        for name in cls.train_sets:
            Processor.download(name)
        for name in cls.test_sets:
            Processor.download(name)

    @classmethod
    def _convert_data(cls):
        pass

    @classmethod
    def _split_data(cls):
        pass

    @classmethod
    def _train(cls):
        pass
