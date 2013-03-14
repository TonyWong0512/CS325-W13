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

def dist(v1, v2):
    """The euclidian distance between two vectors v1 and v2"""
    hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    return int(round(hypot))

def cluster_mean(cluster):
    """The mean for a given cluster of nodes"""
    x_m = y_m = 0.0
    for node in cluster:
        x_m += node[0]
        y_m += node[1]
    x_m /= len(nodes)
    y_m /= len(nodes)
    return (x_m, y_m)

def kmeans(nodes, k):
    means = []
    # while ks != previous ks?, need to stop when they match

    # Step 1, choose K as mean of each partition.
    for i in range(k-1):
        # if k = 3, this will assign ks[0] and ks[1]
        means[i] = cluster_mean(nodes[:1/k])
    # ks[2] will get the rest
    means[k] = cluster_mean(nodes[1/k:])

    # Compute distances for each mean
    mins = []
    for z in means:
        # min 1/kth from tuple
        mins[z] = (dist(means[z], nodes) for i in range(1, len(nodes))

    #    print dist(nodes[0], nodes[x])
    #print i

def main():
    nodes = [(1, 3), (3, 6), (5, 3), (2, 2)]
    kmeans(nodes, 2)
    #nodes2 = [(0,0),(0,1),(1,1),(1,0)]
    #for x in range(1,len(nodes)):
    #    print dist(nodes[0], nodes[x])
    #print cluster_mean(nodes)
    #print dist(nodes[0],nodes[1])

if __name__ == "__main__":
    main()
