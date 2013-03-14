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

def dict_max(ds):
    return max(d.iterkeys(), key=(lambda key: d[key]))

# XXX Current busted. Dicts are sets and keys will get overridden
# Will work for some small k though...
def furthest_nodes2(nodes, k):
    """
    Given a set of nodes, and a k, compute k nodes with the maximum
    distance from each other.

    >>> max_points([(1,2),(3,4)], 2)
    [(1, 2), (3, 4)]
    >>> max_points([(0,0),(0,2),(2,2),(2,0)], 2)
    [(0, 0), (2, 2)]
    """
    k_nodes = []
    k_nodes.append(nodes[0])
    # Compute the maximum distance between k_nodes and nodes
    for i in range(k-1):
        m_nodes = {}
        # Compute diances between k_nodes and nodes
        for node in nodes:
            k_max = {}
            for k_n in k_nodes:
                k_max[node] += dist(k_n, node)

            if k_max:
                maxs = dict_max(k_max)

        if m_nodes:
            # m_nodes is not empty
            max_node = max(m_nodes.iterkeys(), 
                key=(lambda key: m_nodes[key]))
            ks.append(max_node)
    return ks

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
            m_nodes[node] = dist(ks[i], node)

        if m_nodes:
            # m_nodes is not empty
            max_node = max(m_nodes.iterkeys(), 
                key=(lambda key: m_nodes[key]))
            ks.append(max_node)
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
