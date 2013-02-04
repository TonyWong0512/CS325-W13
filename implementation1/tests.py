#! /usr/bin/env python
"""
Inversions

Count the number of elements in a list that are less than other elements
Example: [1, 4, 2, 5, 3]

    There are 3 inversions: (4, 2), (4, 3), (2, 5)
    
Note: This assumes the last element in the list is the total count of
inversions
"""
from brute_force import brute_force as algo
#from naive_dc import naive_dc as algo

# Build a list of lists of ints, each lists last element is the number
# of inversions in that list
lists = [[int(x) for x in line.split(',')] for line in open('sample_results').readlines()]

a1 = [1,2,3,4,5, 0]
a2 = [1,4,2,5,3, 3]
a3 = [5,4,3,2,1, 10]

def main():
    # Append the sample lists
    [lists.append(a) for a in (a1,a2,a3)]

    # Print inversion counts for each list
    counts = [(algo(l[:-1]), l[len(l)-1]) for l in lists]
    for i, j in counts:
        assert i == j, "Inversion count off: i:%d, j:%d" % (i,j)

    print counts

if __name__ == "__main__":
    main()
