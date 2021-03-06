import math
import itertools
import re
import pp

from kmeans import kmeans_pp, associate_points
from glue import edges_in_clusters, glue, center_f

def dist(v1,v2):
    #hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    #return int(round(hypot))
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    return int(round(math.sqrt(dx*dx + dy*dy)))

def wrapped_nearest_neighbor(nodes):
    best_tour = nearest_neighbor(nodes, 0)
    min_length = tour_length(best_tour)
    for i in xrange(1, len(nodes)):
        tour = nearest_neighbor(nodes, i)
        length = tour_length(tour)
        if length < min_length:
            best_tour = tour
    return best_tour


def nearest_neighbor(nodes,start):
    """Create a greedy tour"""
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

def tour_length(tour):
    """Compute the length of the given tour of a graph"""
    length = 0
    for i in range(len(tour)):
        length += dist(tour[i],tour[i-1])
    return length

def build_dict_of_cities(filename):
    """Build a mapping of a node's label to it's points so that the
    node label can be looked up later"""
    f = open(filename,'r')
    cities = {}
    for line in f.readlines():
        line = line.lstrip(' ')
        items = [int(x) for x in re.split('\s+',line) if re.match('\d',x)]
        cities[items[0]] = (items[1],items[2])
    f.close()
    #for key,value in cities.iteritems():
    #    print key, value
    return cities

def reverse(d):
    """Swap the keys and values of a dictionary d"""
    d1 = {}
    for k,v in d.iteritems():
        if v not in d1:
            d1[v] = [k]
        else:
            # Accomodate multiple cities at one location
            d1[v].append(k)
    return d1

def tour_output(tour,filename):
    """Output the tour of a graph"""
    length = tour_length(tour)
    cities = reverse(build_dict_of_cities(filename))
    output = []
    for coords in tour:
        for city in cities[coords]:
            output.append(city)
        if len(cities[coords]) > 1: #if there are multiple values, at same coords,
            cities[coords] = []   #clear list so they are not added twice
    output_file = re.sub("input","output",filename)
    out = "\n".join(str(x) for x in output)
    f = open(output_file,'w')
    f.write(str(length))
    f.write("\n")
    f.write(out)
    f.write("\n")
    f.close()

def two_opt(tour):
    """Compute the minimum tour of a neighborhood by using 2-OPT"""
    min_length = tour_length(tour)
    nodes = len(tour)
    if nodes >= 4:
        min_tour = tour
        for i in xrange(1,nodes):
            new_tour = swap_edges(tour, i, nodes)
            new_length = tour_length(new_tour)
            if new_length < min_length:
                min_length = new_length
                min_tour = new_tour
        return min_tour
    return tour

def swap_edges(tour, mid1, mid2):
    """
    >>> swap_edges([0,1,2,3,4,5,6,7],2,6)
    [0, 1, 5, 4, 3, 2, 6, 7]
    """
    a = tour[:mid1]
    b = tour[mid1:mid2]
    b.reverse()
    c = tour[mid2:]
    return a+b+c

def readinstance(filename):
    # each line of input file represents a city given by three integers:
    # identifier x-coordinate y-coordinate (space separated)
    # city identifiers are always consecutive integers starting with 0
    # (although this is not assumed here explicitly,
    #    it will be a requirement to match up with the solution file)
    f = open(filename,'r')
    line = f.readline()
    cities = []
    while len(line) > 1:
        lineparse = re.findall(r'[^,;\s]+', line)
        cities.append(tuple([int(lineparse[1]),int(lineparse[2])]))
        line = f.readline()
    f.close()
    return cities

def parallel_two_opt_and_nearest_neighbor(cluster):
    best_local = wrapped_nearest_neighbor(cluster)
    return two_opt(best_local)


def pop_main():
    filename = "test-input-3.txt"
    nodes = readinstance(filename)
    job_server = pp.Server(ncpus=7)

    # Create clusters of k
    k = 20
    k_clusters = associate_points(nodes, kmeans_pp(nodes, k))

    depfuncs=(wrapped_nearest_neighbor, two_opt, dist, swap_edges, nearest_neighbor, tour_length)
    modules=("math","itertools")
    jobs = [job_server.submit(parallel_two_opt_and_nearest_neighbor,
                              (cluster,),
                              depfuncs,
                              modules) for cluster in k_clusters.values()]
    clusters = []
    for cluster in jobs:
        clusters.append(cluster())
        print "job %s has run" % id(cluster)

    # Cluter Gluing
    candr = center_f(clusters)

    cluster_tour = nearest_neighbor([k for k in candr],0)
    better = two_opt(cluster_tour)
    tours = glue(candr,better)

    tour_output(tours, filename)

def main():
    filename = "test-input-1.txt"
    nodes = readinstance(filename)
    job_server = pp.Server()

    depfuncs=(wrapped_nearest_neighbor, two_opt, dist, swap_edges, nearest_neighbor, tour_length)
    modules=("math","itertools")
    jobs = [job_server.submit(parallel_two_opt_and_nearest_neighbor,
                              (nodes,),
                              depfuncs,
                              modules)]
    clusters = []
    for cluster in jobs:
        clusters.append(cluster())
        print "job %s has run" % id(cluster)

    # Cluter Gluing
    candr = center_f(clusters)

    cluster_tour = nearest_neighbor([k for k in candr],0)
    better = two_opt(cluster_tour)
    tours = glue(candr,better)

    tour_output(tours, filename)




    
if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    pop_main()


