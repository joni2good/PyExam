import random
import time


def estimate_pi(p):
    num_in = 0
    num_total = 0
    for point in range(p):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        dist = x**2 + y**2
        if dist < 1:
            num_in += 1
        num_total += 1
    return 4 * num_in / num_total


# print(estimate_pi(10))
# print(estimate_pi(100))
# print(estimate_pi(1000))
# print(estimate_pi(10000))
# print(estimate_pi(100000))
# print(estimate_pi(1000000))
# print(estimate_pi(10000000))
# t1 = time.time()
# print(estimate_pi(100000000))
# t2 = time.time()
# t3 = t2 - t1
# print(t3)
