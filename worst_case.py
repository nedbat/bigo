import time

import numpy


def time_make_set(number, step, tries=5):
    start = time.time()
    for _ in range(tries):
        s = set(i * step for i in range(number))
    end = time.time()
    return end - start

for step in ["1234567", "2**61-1"]:
    stepnum = eval(step)
    for number in range(1, 6):
        t = time_make_set(number * 10000, stepnum)
        print(f"{step:9} {number} {t:9.3f}s")

def do_a_bunch(step, numpoints, item_step):
    sizes = []
    times = []
    for size in range(step, step*numpoints, step):
        t = time_make_set(size, item_step)
        sizes.append(size)
        times.append(t*1000)

    return numpy.polyfit(numpy.array(sizes), numpy.array(times), 2)

if 0:
    print(do_a_bunch(50000, 30, 47))
    print(do_a_bunch(1000, 20, 2**61-1))
