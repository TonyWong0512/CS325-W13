import math
import itertools

def dist(v1,v2):
    #hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    #return int(round(hypot))
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    return int(round(math.sqrt(dx*dx + dy*dy)))

def brute_glue(clusters):
    all_edges = [list(itertools.chain(*cluster)) for cluster in clusters]
    glue = []
    for cluster in clusters:
        valid = all_edges.remove(cluster)
        small = dist(cluster[0],valid[0])
        temp_glue
        for node in cluster:
            for node1 in valid:
                distance = dist(node,node1)
                if distance < small and (node,node1) not in glue:
                    small = distance
                    temp_glue = (node,node1)
            glue.append((node,node1))

def closest_between_two_clusters(cluster1,cluster2):
    pass # returns two points, one in each cluster

def index_of_node(cluster,node):
    return(cluster.index(node))

def shortest_two_edges(cluster1,cluster2,node1,node2):
    (node1, node2) = closest_between_two_clusters(cluster1,cluster2)
    pass # returns the four nodes, node1 -> node 2, node3 -> node4

def glue(d,centers):
    order = [[d[center]] for center in centers]
    closest = {}
    for i,cluster in enumerate(order):
        previous = order[i-1]
        (node1,node2,node3,node4) = shortest_two_edges(cluster,previous)
        
        
        '''
            find closest edges between the appropriate nodes, one in each cluster
            identify the two shortest edges between the four/six nodes in question
            make those two edges happen, like magic, bitch
        '''
    
def two_opt(foo):
    pass

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
