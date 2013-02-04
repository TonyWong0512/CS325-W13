#! /usr/bin/env python
"""
Inversion Counting - Brute Force

This algorithm works simply by checking all possible pairs of elements
to count the total inversions.
"""
def brute_force(lst):
    invs = []
    brute_force_helper(lst, invs)
    return len(invs)

def brute_force_helper(lst, invs):
    """ Brute force method for counting inversions """
    for i in range(0, len(lst)):
        # i+i ensures the element is not compared against itself
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                invs.append((lst[i], lst[j]))
    return lst

#def main():
#    print brute_force([1,4,2,5,3])
#
#if __name__ == "__main__":
#    main()
