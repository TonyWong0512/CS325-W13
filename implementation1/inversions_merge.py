#! /usr/bin/env python
"""
Inversion Counting - Merge and Count

Count the number of elements in a list that are less than other elements
Example: [1, 4, 2, 5, 3]

    There are 3 inversions: (4, 2), (4, 3), (2, 5)
    
Note: This assumes the last element in the list is the total inver of
inversions
"""
# Build a list of lists of ints
lists = [[int(x) for x in line.split(',')] for line in open('test_input.txt').readlines()]
inver = 0

def merge_sort(lis):
    if len(lis) < 2: return lis 
    m = len(lis) / 2 
    return merge_count_inversion(merge_sort(lis[:m]), merge_sort(lis[m:])) 

def merge_count_inversion(left, right):
    global inver
    sorted_results = [] 
    i = j = 0 
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            sorted_results.append(left[i])
            i += 1 
        else: 
            sorted_results.append(right[j])
            inver = inver + (len(left) - i)
            j += 1
    sorted_results.extend(left[i:]) 
    sorted_results.extend(right[j:]) 
    return sorted_results

for l in lists:
	merge_sort(l)
	print inver
	inver = 0 

