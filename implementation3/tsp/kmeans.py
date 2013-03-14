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


# XXX Current busted. Dicts are sets and keys will get overridden
# Will work for some small k though...
def furthest_nodes(nodes, k):
    """
    Given a set of nodes, and a k, compute k nodes with the maximum
    distance from each other.

    >>> max_points([(1,2),(3,4)], 2)
    [(1, 2), (3, 4)]
    >>> max_points([(0,0),(0,2),(2,2),(2,0)], 2)
    [(0, 0), (2, 2)]
    """
    ks = []
    ks.append(nodes[0])
    # Ignore 1 k since we are starting with one
    for i in range(k-1):
        m_nodes = {}
        for node in (n for n in nodes if n not in ks):
            # key: distance, value: node
            m_nodes[dist(ks[i], node)] = node

        if m_nodes:
            # m_nodes is not empty
            max_key = max(m_nodes.keys())
            # node with maximum distance away
            ks.append(m_nodes[max_key])
    return ks

def dist(v1, v2):
    """The euclidian distance between two vectors v1 and v2
    >>> dist((0,0),(3,4))
    5
    """
    hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    return int(round(hypot))

def main():
    lists = [tuple([int(x) for x in line.split(' ')])[1:] for line in open('example-input-1.txt').readlines()]
    print furthest_nodes(lists, 4)

def test():
    """Run doctests"""
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    #test()
    main()
