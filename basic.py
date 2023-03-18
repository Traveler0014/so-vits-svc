import os


def split_path(path: str):
    dirname = os.path.dirname(path)
    name, ext = os.path.splitext(os.path.basename(path))
    ext = ext.casefold()
    return dirname, name, ext

def join_path(dirname: str, name: str, ext: str):
    dirname = os.path.abspath(dirname)
    filename = '{}{}'.format(name, ext)
    return os.path.join(dirname, filename)

def to_ext(path: str, ext: str):
    if not ext.startswith('.'): ext = f'.{ext}'
    dirname, name, _ = split_path(path)
    return join_path(dirname, name, ext)

def get_dir(path: str):
    return split_path(path)[0]


def get_name(path: str):
    return split_path(path)[1]


def get_ext(path: str):
    return split_path(path)[2]