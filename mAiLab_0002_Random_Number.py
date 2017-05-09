import random
import numpy as np
import time

# 1. Generate five random numbers and print them out.

print([random.random() for i in range(5)])

# 2. Generate N random numbers within 1 and -1.
#    Calaulate the mean and stddey of them and print the results out.
#    N = 10^1, 10^2, 10^3, 10^4, 10^5

def randomNumber(N):
    # 2 * [0, 1) - 1 -> [-1, 1)
    return 2 * np.random.random_sample(N) - 1

N = [10 ** i for i in range(1, 6)]
for i in N:
    start_time = time.time()
    random_number = randomNumber(i)
    finish_time = time.time()
    print("Avg. {}".format(random_number.mean()))
    print("Stddev. {}".format(random_number.std()))
    print("Time {:6f}s".format(finish_time - start_time))