import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def faster_calculate(value):
    p = Pool(processes=4)
    return sum(p.map(slow_calculate, range(value)))


def timer():
    start_time = time.time()
    faster_calculate(5)
    timer = int("%d" % (time.time() - start_time))
    return timer


if __name__ == "__main__":
    timer()
