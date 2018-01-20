import os
import errno
import pathlib

def make_not_exist(path):
    print(path)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    return path
