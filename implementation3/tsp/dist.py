import math, re, sys

def dist(c1, c2):
    hypot = math.hypot(c1[0]-c1[1], c2[0]-c2[1])
    return int(round(hypot))

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
        cities.append([int(lineparse[1]),int(lineparse[2])])
        line = f.readline()
    f.close()
    return cities

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python dist.py inputfilename"
        exit(-1)
    input_file = sys.argv[1]
    cities = readinstance(input_file) # maybe later optimize to list of tuples
    print dist((1,2),(1,3))
