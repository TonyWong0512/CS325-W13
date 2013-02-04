#! /usr/bin/env python
import time

from random import randrange
from itertools import chain
from brute_force import brute_force
from naive_dc import naive_dc

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
            print "%f ms" % self.msecs

def inversion_analysis(func):
    print func.__name__
    print "-----------"
    for i in chain(range(1,6),range(10,60,10)):
        print "%d:" % (1000*i),
        lst = []
        for j in range(1,1000*i):
            lst.append(randrange(1,1000*i))
        #print lst,

        with Timer() as t:
            func(lst)
    print

def main():
    inversion_analysis(brute_force)
    inversion_analysis(naive_dc)
   
if __name__ == "__main__":
    main()
