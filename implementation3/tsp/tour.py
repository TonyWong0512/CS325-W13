import math
import itertools

def dist(v1,v2):
    hypot = math.hypot(v1[0]-v2[0], v1[1]-v2[1])
    return round(hypot)

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

def two_opt(tour):
    while True:
        best = tour
        # for all possible edge pairs in T
        pairs = itertools.combinations(tour,2)
        for pair in pairs:
            print pair
        '''for i in range(len(pairs-1)):
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


def main():
    lists = [tuple([int(x) for x in line.split(' ')])[1:] for line in open('example-input-1.txt').readlines()]
    tour = nearest_neighbor(lists,0)
    #print tour
    two_opt(tour)

if __name__ == "__main__":
    main()

