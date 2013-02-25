#! /usr/bin/env python
import random
import time
from brute_sum import brute_sum as brute
from dynamic import dynamic as dynamic
from divide_conquer import divide_conquer as divide

test_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
f = open('test_output','w')
def run_test(algo):
    for i in test_sizes: 
        test_data = []
        for _ in range(i):
            test_data.append(random.randint(-i,i))
        before = time.time()
        algo(test_data)
        after = time.time()
        duration = after-before
        f.write(str(i))
        f.write(",")
        f.write(str(duration))
        f.write("\n")

if __name__ == "__main__":
    f.write("Brute\n")
    run_test(brute)
    f.write("Dynamic\n")
    run_test(dynamic)
    f.write("Divide\n")
    run_test(divide)
