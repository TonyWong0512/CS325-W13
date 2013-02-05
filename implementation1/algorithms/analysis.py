#! /usr/bin/env python
import time

from random import randrange
from itertools import chain
from brute_force import brute_force
from naive_dc import naive_dc
from inversions_merge import merge_sort

class Timer(object):
    def __init__(self, verbose=True):
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

def inversion_analysis(func):
    print func.__name__
    print "-----------"
    # Input arrays of size 1k, 2k, 3k, 4k, 5k, and 10k, 20k, 30k, 40k,
    # 50k respectively
    for i in chain(xrange(1,6),xrange(10,60,10)):
        # For each size, generate 10 random inputs
        print "%d:\t" % (1000*i),
        for z in xrange(10):
            lst = []
            for j in xrange(1,1000*i):
                # Random permutations of numbers 1,...,n where n is the
                # input size
                lst.append(randrange(1,1000*i))

            with Timer() as t:
                func(lst)
            del lst
        print
    print

def main():
    inversion_analysis(brute_force)
    inversion_analysis(naive_dc)
    inversion_analysis(merge_sort)
   
if __name__ == "__main__":
    main()
