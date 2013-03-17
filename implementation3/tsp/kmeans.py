#! /usr/bin/env python
"""
Given a number of partitions k (k>=2), create X_k arbitrary points. Then
compute all distances from each X_k point such that 1/kth of them are
associated with X_k, then move X_k to the x,y mean of all of it's
associted points.

Recomputing several times will put X_k closer to a cluster.

Increasing K will give better approximations up to some 'elbow' point.
This point is the point of the graph of number of iterations before X_k
does not change.
"""
import math

def kmeans_pp(nodes, k):
    """kmeans++

    Doesn't actually compute kmeans, just does the setup of ++

    Returns k central points

    >>> kmeans_pp([(1,2),(3,4)], 2)
    [(1, 2), (3, 4)]

    >>> kmeans_pp([(0,0),(0,2),(2,2),(2,0)], 4)
    [(0, 0), (2, 2), (0, 2), (2, 0)]
    """
    assert(k >= 2)
    assert(len(nodes) > 0)

    # Don't want to have any array bound errors
    ks = []

    # Choose the first center point
    ks.append(nodes[1])

    # Find the farthest point from it
    while len(ks) != k:
        kmax = dist(ks[0], nodes[0])
        max_node = nodes[0]

        for node in (node for node in nodes if node not in ks):
            possible = 0.0

            for knode in ks:
                possible += dist(knode, node)

            if possible > kmax:
                kmax = possible
                max_node = node
        ks.append(max_node)

    return ks

def associate_points(nodes, ks):
    """Create a dictionary with points associated with ks

    >>> associate_points([(0,0),(2,2),(3,4),(10,-1)], [(2,2)])
    {(2, 2): [(2, 2), (0, 0), (3, 4), (10, -1)]}
    >>> associate_points([(0,0),(1,1),(2,2),(3,4),(10,-1)], [(3,4), (0,0)])
    {(0, 0): [(0, 0), (1, 1)], (3, 4): [(3, 4), (2, 2), (10, -1)]}
    """
    k_dict = {}
    for k in ks:
        k_dict[k] = [k]

    for node in (n for n in nodes if n not in ks):
        m_dist = dist(node, ks[0])
        k_node = ks[0]
        for k in ks:
            k_dist = dist(k, node)
            if k_dist < m_dist:
                m_dist = k_dist
                k_node = k
        k_dict[k_node].append(node)
    return k_dict


def dist(v1, v2):
    """The euclidian distance between two vectors v1 and v2
    >>> dist((0,0),(3,4))
    5
    >>> dist((0,0),(9,40))
    41
    >>> dist((0,0),(5,12))
    13
    """
    return int(round(math.hypot(v1[0]-v2[0], v1[1]-v2[1])))

def main():
    lists = [tuple([int(x) for x in line.split(' ')])[1:] for line in open('example-input-1.txt').readlines()]
    ap = associate_points(lists, kmeans_pp(lists, 8))
    from pprint import pprint
    pprint(ap, indent=2)


def test():
    """Run doctests"""
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    #test()
    main()
