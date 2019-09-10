from os import listdir
from os.path import isfile, join


def get_lst_file(directory, get_ext=True):
    if get_ext:
        files = [f for f in listdir(directory) if isfile(join(directory, f))]
    else:
        files = [f.split('.')[0] for f in listdir(directory) if isfile(join(directory, f))]
    files.sort()
    return files