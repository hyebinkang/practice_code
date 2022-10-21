t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for i in range(n):
        c1, c2, r = map(int, input().split())
        d1 = (c1-x1)**2 + (c2-y1)**2            #x1,y1을 기준으로 c1과 c2의 거리(출발)
        d2 = (c1-x2)**2 + (c2-y2)**2            #x2, y2를 기준으로 c1과 c2거리(도착)

        circle = r**2                           #원의 넓이

        if circle > d1 and circle > d2:         #행성 중심과의 거리가 모두 행성의 반지름 보다 작은 경우
            pass
        elif circle > d1:                       #출발점이 행성 중심보다 작은 경우
            count +=1
        elif circle >d2:                        #도착점이 행성 중심 보다 큰 경우
            count +=1

    print(count)
