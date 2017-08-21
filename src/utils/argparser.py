from constants import Constants
import argparse
import sys

class ArgParser(object):
    """
    Parse args in main
    """

    parser = argparse.ArgumentParser(
        description='A python program trains or serves object recognition models.')
    parser.add_argument(Constants.MODE, help='Running mode', choices=Constants.MODES)

    @classmethod
    def parse(cls):
        # print help text if no args
        if len(sys.argv) == 1:
            sys.argv.append('-h')

        return vars(cls.parser.parse_args())
