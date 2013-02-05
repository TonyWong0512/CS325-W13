#! /usr/bin/env python
"""
Inversion Counting - Merge and Count

Count the number of elements in a list that are less than other elements
Example: [1, 4, 2, 5, 3]

    There are 3 inversions: (4, 2), (4, 3), (2, 5)
    
Note: This assumes the last element in the list is the total inver of
inversions
"""
def merge_sort(lst):
    invs = [0]
    _merge_sort(lst, invs)
    return invs[0]

def _merge_sort(lis, invs):
    if len(lis) < 2:
        return lis

    m = len(lis) / 2 

    return merge_count_inversion(
        _merge_sort(lis[:m], invs),
        _merge_sort(lis[m:], invs),
        invs)

def merge_count_inversion(left, right, invs):
    sorted_results = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_results.append(left[i])
            i += 1
        else: 
            sorted_results.append(right[j])
            invs[0] += len(left) - i
            j += 1
    sorted_results.extend(left[i:])
    sorted_results.extend(right[j:])
    return sorted_results
