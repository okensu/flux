from argparse import ArgumentParser, ArgumentTypeError
from os.path import isfile

def _config_file(config_path):
    if not isfile(config_path):
        raise ArgumentTypeError("configuration file doesn't exist!")

    return config_path

def parse_arguments():
    parser = ArgumentParser(
        description='Train a Flux LoRA using the provided configuration file.',
        epilog='Made with ❤️ by okensu.'
    )

    parser.add_argument(
        'config_path',
        type=_config_file,
        help='Relative or absolute path to configuration file (e.g.: ./path/to/config.yaml or /home/user/path/to/config.yaml or C:\\path\\to\\config.yaml).'
    )

    args = parser.parse_args()

    return args
