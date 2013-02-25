#! /usr/bin/env python
import time

from random import randrange
from itertools import chain
from brute_sum import brute_sum
from divide_conquer import divide_conquer
from dynamic import dynamic

f = open("test_output", 'w',1)

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000 #millisecs
        if self.verbose:
            print "%f" % self.msecs,
        #return self.msecs

    def msecs(self):
        return self.msecs

def sum_analysis(func):
    f.write("%s\n" % func.__name__)
    f.write("-----------\n")
    # Input arrays of size 1k, 2k, 3k, 4k, 5k, and 10k, 20k, 30k, 40k,
    # 50k respectively
    for i in xrange(1,11):
        avg = []
        # For each size, generate 10 random inputs
        for z in xrange(10):
            lst = []
            r = i*1000
            for j in xrange(1,r):
                # Random permutations of numbers 1,...,n where n is the
                # input size
                lst.append(randrange(-r,r))

            with Timer() as t:
                func(lst)
            del lst
            avg.append(t.msecs)
        f.write("(%d, %f)\n" % ((1000*i), (sum(avg)/float(len(avg)))))
    f.write('\n')

def main():
    sum_analysis(divide_conquer)
    sum_analysis(dynamic)
    sum_analysis(brute_sum)
   
if __name__ == "__main__":
    main()
