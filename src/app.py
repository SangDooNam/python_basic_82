import os


class FileNotFoundError(Exception):
    pass


def rm(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError("The file doesn't exit")
    else:
        os.remove(filename)
        




