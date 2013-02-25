#! /usr/bin/env python
"""
Maximum Subarray - Divide & Conquer

This algorithm will find the largest subarray in an array.

The largest subarray will be either fully contained in the first half,
or fully contained in the second half, or consisting of a suffix of the
first half and a prefix of the second half.

The first two cases can be found recursively. The last case can be found
in linear time.
"""

def divide_conquer(lst):
    if len(lst) < 2:
        return lst[0]

    if len(lst) == 2:
        return max(sum(lst), lst[0])

    mid = len(lst)/2

    left = divide_conquer(lst[0:mid+1])
    right = divide_conquer(lst[mid:len(lst)])

    l1 = lst[0:mid]
    l2 = lst[mid:len(lst)]

    m_left = l1[len(l1)-1]
    s = 0
    for x in reversed(l1):
        s += x
        m_left = max(m_left, s)

    m_right = l2[0]
    s = 0
    for y in l2:
        s += y
        m_right = max(m_right, s)

    return max(left, right, (m_left+m_right))


def test_algo(algo):
    l1 = [1,2,3,-4,5] # Max: 1, 2, 3, -4, 5 => 7
    l2 = [1,2,3,4,5] # Max: 1, 2, 3, 4, 5 => 15

    l3 = [-371,-287,978,738,-766,836,899,521,-505,31,-387,-60,396,110,4,855,927,580,495,-269,146,890,914,860,-269,125,-921,-806,-339,647,137,592,322,622,-497,294,166,-109,-899,764,-160,969,15,923,361,729,-635,-827,916,-39,464,635,-453,-772,196,845,181,-929,215,262,520,708,550,14,82,-284,14,-93,304,-586,-524,937,104,-834,81,-9,146,-452,-838,791,120,-695,-468,930,-132,607,247,-551,-65,205,-630,-215,68,-737,46,327,-478,-582,-363,895] #12792

    l4 = [-180,885,-827,826,-274,895,638,751,-776,-666,-595,-123,590,-148,827,-599,-527,-711,557,660,54,-695,681,-80,-130,235,-445,-235,-627,795,-378,447,176,30,382,451,-33,-139,766,-731,319,488,646,-972,-750,-843,346,16,-227,774,976,-780,-447,-130,-34,-127,-112,-673,462,-381,-823,190,428,-398,-43,-619,757,-972,-376,232,-50,-748,-527,-674,913,588,822,-854,-946,689,740,-547,-861,-151,-185,789,359,-698,548,-480,864,-948,-137,-109,457,925,-744,-248,-399,230] #3360

    l5 = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84] # 187
    l6 = [-1, -2, -3, -4, -5] # -1

    assert(algo(l1) == 7)
    assert(algo(l2) == 15)
    assert(algo(l3) == 12792)
    assert(algo(l4) == 3360)
    assert(algo(l5) == 187)
    assert(algo(l6) == -1)

if __name__ == "__main__":
    test_algo(divide_conquer)
    print "Algorithm Correct"
