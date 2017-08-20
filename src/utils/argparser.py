import argparse
import sys

class ArgParser(object):

    parser = argparse.ArgumentParser(
        description='A python program trains or serves object recognition models.',
        usage='./scripts/run.sh [Options] Command')

    parser.add_argument('train', help='Train a model')

    @classmethod
    def parse(cls):

        # print help text if no args
        if len(sys.argv) == 1:
            sys.argv.append('-h')

        print cls.parser.parse_args()
