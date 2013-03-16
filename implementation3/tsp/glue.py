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
        
def glue(d,centers):
    order = [[d[center]] for center in centers]
    closest = {}
    for cluster in order:
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
