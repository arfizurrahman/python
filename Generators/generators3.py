from time import time


def perfomance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@perfomance
def long_time():
    print('1')
    for i in range(10000000):
        i*5


@perfomance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5


long_time()
long_time2()
