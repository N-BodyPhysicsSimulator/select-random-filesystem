from os.path import isfile, isdir, join, abspath
from os import walk, sep
from random import shuffle

FILE = 0
DIR = 1
DIRECTORY = DIR

__all__ = ['get_item', 'get_dir', 'get_directory', 'FILE', 'DIR', 'DIRECTORY']

def get_item(type, base_dir=None):
    if base_dir is None:
        base_dir = abspath(sep)

    for path, dirs, files in walk(base_dir):
        if len(files) > 0 and type is FILE:
            for file in files:
                joined = join(base_dir, file)
                if isfile(joined):
                    return joined

        elif len(dirs) > 0 and type is DIRECTORY:
            for dir in dirs:
                joined = join(base_dir, dir)
                if isdir(joined):
                    return joined

    return None

def get_file(base_dir=None):
    return get_item(FILE, base_dir)

def get_directory(base_dir=None):
    return get_item(DIRECTORY, base_dir)

def get_dir(base_dir=None):
    return get_directory(base_dir)
