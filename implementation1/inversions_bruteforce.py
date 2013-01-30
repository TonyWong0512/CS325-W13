#! /usr/bin/env python
"""
Inversion Counting - Brute Force

Count the number of elements in a list that are less than other elements
Example: [1, 4, 2, 5, 3]

    There are 3 inversions: (4, 2), (4, 3), (2, 5)
    
"""
# Build a list of lists of ints
lists = [[int(x) for x in line.split(',')] for line in open('sample_results').readlines()]

a1 = [1,2,3,4,5]
a2 = [1,4,2,5,3]
a3 = [5,4,3,2,1]

def main():
    # Append the sample lists
    [lists.append(a) for a in (a1,a2,a3)]

    # Print inversion counts for each list
    print [inv_count(l) for l in lists]


def inv_count(lst):
    """ Brute force method for counting inversions """
    inv = []
    for i in range(0, len(lst)):
        # i+i ensures the element is not compared against itself
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                inv.append((lst[i], lst[j]))
    return len(inv)
        

if __name__ == "__main__":
    main()
