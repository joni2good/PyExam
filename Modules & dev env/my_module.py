import random
import time


def estimate_pi(p):
    num_in = 0
    num_total = 0
    for point in range(p):
        # x = random.uniform(0, 1)
        # y = random.uniform(0, 1)
        # above and below are the same
        x = random.random()
        y = random.random()
        dist = x**2 + y**2
        if dist < 1:
            num_in += 1
        num_total += 1
    return 4 * num_in / num_total


def time_me(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(f"{func.__name__} finished in {t2 - t1} seconds")
        return result
    return wrapper
