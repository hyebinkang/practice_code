import math
def circle(r):

    print(format(r*r*math.pi, ".6f"))
    print(format(r*r*2, ".6f"))

    return r

circle(int(input()))