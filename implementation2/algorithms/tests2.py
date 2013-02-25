#! /usr/bin/env python
"""
Maximum Subarray Tests
"""
from brute_sum import brute_sum as algo
#from divide_conquer import divide_conquer as algo
#from dynamic import dynamic as algo

# Build a list of lists of ints, each lists last element is the number
# of sums in that list
#lists = [[int(x) for x in line.split(',')] for line in open('test_input.txt').readlines()]
lists = [[int(x) for x in line.split(',')] for line in open('test_input2.txt').readlines()]

def main():
    # Check sums
    sums = [(algo(l[:-1]), l[-1]) for l in lists]
    for i, j in sums:
        assert i == j, "Sums off: i:%d, j:%d" % (i,j)

    print "Sums Correct"

def create_sums():
    for i in (algo(lst) for lst in lists):
        print i

if __name__ == "__main__":
    main()
    #create_sums()
