import math
import itertools
import re

def dist(v1,v2):
    #hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    #return int(round(hypot))
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    return int(round(math.sqrt(dx*dx + dy*dy)))

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

def tour_length(tour):
    length = 0
    for i in range(len(tour)):
        length += dist(tour[i],tour[i-1])
        print length, tour[i], tour[i-1]
    #length+= dist(tour[0],tour[-1]) #and dist to go to start
    return length

def build_dict_of_cities(filename):
    f = open(filename,'r')
    cities = {}
    for line in f.readlines():
        line = line.lstrip(' ')
        items = [int(x) for x in re.split('\s+',line) if re.match('\d',x)]
        cities[items[0]] = (items[1],items[2])
    f.close()
    return cities

def reverse(d): #switch keys and values
    d1 = {}
    for k,v in d.iteritems():
        if v not in d1:
            d1[v] = [k]
        else: #accomodates multiple cities at one location
            d1[v].append(k)
    return d1

def tour_output(tour,filename):
    length = tour_length(tour)
    cities = reverse(build_dict_of_cities(filename))
    output = []
    for coords in tour:
        for city in cities[coords]:
            output.append(city)
        if len(cities[coords]) > 1: #if there are multiple values, at same coords,
            cities[coords] = []   #clear list so they are not added twice
    output_file = re.sub("input","testoutput",filename)
    output.sort()
    out = "\n".join(str(x) for x in output)
    f = open(output_file,'w')
    f.write(str(length))
    f.write("\n")
    f.write(out)
    f.close()

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
    filename = "example-input-1.txt"
    lists = readinstance(filename)
    tour = nearest_neighbor(lists,0)
    tour_output(tour,filename)
    #print tour
    two_opt(tour)

if __name__ == "__main__":
    main()

