import math
import itertools

from kmeans import dist

"""
def dist(v1,v2):
    hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    return int(round(hypot))
"""

def edges_in_clusters(cluster1,cluster2):
    #returns the index of some close nodes between two clusters
    best_nodes = (cluster1[0],cluster2[0])
    smallest = dist(best_nodes[0],best_nodes[1])
    for edge1 in cluster1:
        for edge2 in cluster2:
            distance = dist(edge1,edge2)
            if distance < smallest:
                smallest = distance
                best_nodes = (edge1,edge2)
    indexes = (cluster1.index(best_nodes[0]), cluster2.index(best_nodes[1]))
    return (indexes[0],indexes[1],indexes[0],indexes[1])

def glue(d,centers):
    order = [d[center] for center in centers]
    mega = order.pop()
    for cluster in order:
        (node1,node2,node3,node4) = edges_in_clusters(cluster,mega)
        #mega = mega[:node1] + cluster[node4:0] + cluster[-1:node2] + mega[node3:]
        cluster.reverse()
        mega = mega[:node1] + cluster + mega[node3:]
        #mega += cluster
    print len(mega)
    return mega
    
def center_f(clusters):
    centers = {}
    for i, cluster in enumerate(clusters):
        size = len(cluster)
        x = sum(edge[0] for edge in cluster)/size
        y = sum(edge[1] for edge in cluster)/size
        centers[(x,y)] = cluster
    return centers

"""
centers = center(clusters)
center_to_cluster = {}
for center in centers:
    center_to_cluster[center[0]] = center[1]
cluster_tour = nearest_neighbor(centers[0])
better = two_opt(cluster_tour)
glue(center_to_cluser,better)
"""
