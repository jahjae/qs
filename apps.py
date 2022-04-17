
from multiprocessing import *
import logging
import os

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

def parallel(_func, _parameter):
    Process(target=_func, args=_parameter).start()

