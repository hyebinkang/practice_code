import math
def circle(r):

    print(format(r*r*math.pi, ".6f"))       #유클리드 기하학 원의 넓이 구하기
    print(format(r*r*2, ".6f"))             #택시 기하학 원의 넓이 구하기

    return r

circle(int(input()))