
from multiprocessing import *


def parallel(_func):
    Process(target=_func, args='')