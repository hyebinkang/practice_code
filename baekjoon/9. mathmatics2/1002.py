n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5           #좌표 사이의 길이 구하기 공식

    if distance == 0 and r1 ==r2:                       #distance가 0이고, 반지름 r1,r2가 같으면 같은 원이므로 접점이 무한대
        print(-1)
    elif r1+r2 == distance or abs(r1-r2) == distance:   #원이 외접하거나 내접할 때 접점의 수가 1개
        print(1)
    elif abs(r1-r2) < distance < r1+r2:                 #외접과 내접 사이일 때 접점의 수가 2개
        print(2)
    else:                                               #그 외에 외부에서 만나지 않거나, 내부에서 만나지 않을 때 접점의 수 0개
        print(0)