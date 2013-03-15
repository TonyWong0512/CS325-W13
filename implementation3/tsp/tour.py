import math
import itertools
import re

def dist(v1,v2):
    hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    return int(round(hypot))

def nearest_neighbor(nodes,start):
    tour = [nodes[start]]
    while nodes:
        last = tour[-1]
        closest = dist(last,nodes[start-1])
        closest_node = None
        for node in nodes:
            distance = dist(last,node)
            if distance <= closest and distance != 0:
                closest_node = node
                closest = distance
        tour.append(closest_node)
        nodes.remove(closest_node)
    return tour

def tour_length(tour):
    length = 0
    for i in range(len(tour)-1):
        length += dist(tour[i],tour[i+1])
    return length

def two_opt(tour):
    while True:
        best = tour
        # for all possible edge pairs in T
        pairs = itertools.combinations(tour,2)
        edges = {}
        for pair in pairs:
            if pair[0] not in edges:
                edges[pair[0]] = [pair[1]]
            else:
                edges[pair[0]].append(pair[1])
        '''for vertex in edges:
            
        #   change = tour with ends points swapped
            change = 
            if change < best:
                best = change
                altered = true
        tour = best
        if altered is False:
            break
        '''
        break
    return tour

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

def main():
    #lists = [tuple([int(x) for x in line.split(' ')])[1:] for line in open('example-input-2.txt').readlines()]
    lists = readinstance("example-input-3.txt")
    tour = nearest_neighbor(lists,0)
    print tour_length(tour)
    #print tour
    two_opt(tour)

if __name__ == "__main__":
    main()

