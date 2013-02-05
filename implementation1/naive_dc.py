#! /usr/bin/env python
"""
Inversion Counting - Naive Divide & Conquer

This algorithm will count the inversion by dividing the given array into
two equal-sized subarrays.

To come up with the total inversions it will recursively count the
inversions in each subarray, and then count how many inversions happen
between their merger (by considering each pair).
"""
# Python's ints are immutable even though they get passed by reference,
# so we're using a list of length 1
def naive_dc(lst):
    invs = [0]
    naive_dc_helper(lst, invs)
    return invs[0]

def naive_dc_helper(lst, invs):
    """ Naive Divide & Conquer method for counting inversions """
    if len(lst) < 2:
        return lst

    if len(lst) == 2:
        if lst[0] > lst[1]:
            invs[0] += 1
        return lst

    mid = len(lst)/2

    left = naive_dc_helper(lst[0:mid], invs)
    right = naive_dc_helper(lst[mid:len(lst)], invs)

    return merge(left, right, invs)

def merge(l1, l2, invs):
    """ Count inversions in merge of two lists """
    for lst in ((x,y) for x in l1 for y in l2):
        if lst[0] > lst[1]:
            invs[0] += 1
    return l1 + l2

#def main():
#    print naive_dc([3,1,2])

#if __name__ == "__main__":
#    main()
