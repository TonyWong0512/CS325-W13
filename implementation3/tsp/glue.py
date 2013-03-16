import math
import itertools

def nearest_neighbor(nodes,start):
    tour = [nodes.pop(start)]
    while nodes:
        last = tour[-1]
        closest = dist(last,nodes[0])
        closest_node = None
        for node in nodes:
            distance = dist(last,node)
            if distance <= closest:
                closest_node = node
                closest = distance
        tour.append(closest_node)
        nodes.remove(closest_node)
    return tour

def dist(v1,v2):
    hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    return int(round(hypot))

def index_of_node(cluster,node):
    return(cluster.index(node))

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
    indexes = (index_of_node(cluster1,best_nodes[0]),index_of_node(cluster2,best_nodes[1]))
    return (indexes[0],indexes[1],indexes[0]-1,indexes[1]-1)

def glue(d,centers):
    order = [[d[center]] for center in centers]
    mega = order.pop()
    for i,cluster in enumerate(order):
        (node1,node2,node3,node4) = edges_in_clusters(cluster,mega)
        mega = mega[:node1] + cluster[node4:0] + cluster[-1:node2] + mega[node3:]
    return mega
    
def center(clusters):
    center = []
    order = []
    for cluster in clusters:
        size = len(cluster)
        x = sum(edge[0] for edge in cluster)/size
        y = sum(edge[1] for edge in cluster)/size
        center.append((x,y))
        order.append(cluster)
    return [center,order]

centers = center(clusters)
center_to_cluster = {}
for center in centers:
    center_to_cluster[center[0]] = center[1]
cluster_tour = nearest_neighbor(centers[0])
better = two_opt(cluster_tour)
glue(center_to_cluser,better)
