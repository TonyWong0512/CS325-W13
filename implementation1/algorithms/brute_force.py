#! /usr/bin/env python
"""
Inversion Counting - Brute Force

This algorithm works simply by checking all possible pairs of elements
to count the total inversions.
"""
def brute_force(lst):
    invs = [0]
    brute_force_helper(lst, invs)
    return invs[0]

def brute_force_helper(lst, invs):
    """ Brute force method for counting inversions """
    for i in range(0, len(lst)):
        # i+1 ensures the element is not compared against itself
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                invs[0] += 1
    return lst

#def main():
#    print brute_force([1,4,2,5,3])
#
#if __name__ == "__main__":
#    main()
