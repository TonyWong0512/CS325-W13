import pp
import math

'''def nearest_neighbor(nodes,start=0):
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
'''
def dist(v1,v2):
    #hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    #return int(round(hypot))
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    return int(round(math.sqrt(dx*dx + dy*dy)))

def nearest_neighbor(foo):
    print foo
    #print math.factorial(1000000)
    return sum(foo)
    
def kopt(foo):
    print foo
    return math.sqrt(foo)

def do_it_good(cluster):
    tour = nearest_neighbor(cluster)
    best = kopt(tour)
    return best

clusters = [
    (1,2,3,4,5),
    (6,7,8,9,10),
    (11,12,13,14,15),
    (16,17,18,19,20) ]
job_server = pp.Server()
depfuncs=(nearest_neighbor,kopt,dist)
modules=("math","itertools")
jobs = [job_server.submit(do_it_good,(cluster,),depfuncs,modules) for cluster in clusters]
for job in jobs:
    results = job()
    print "job", results, "has run"
