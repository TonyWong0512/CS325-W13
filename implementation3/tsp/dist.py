import math

def dist(c1, c2):
    hypot = math.hypot(c1[0]-c1[1], c2[0]-c2[1])
    return int(round(hypot))

if __name__ == "__main__":
    print dist((1,2),(1,3))
