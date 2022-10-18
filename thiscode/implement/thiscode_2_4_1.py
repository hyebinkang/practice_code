n = int(input())

x,y = 1, 1                              #시작점
nx, ny = x,y                            #변화하면서 바뀔 점
direction = list(map(str, input().split()))         #방향 입력

for i in direction:
    if i == 'L':
        ny -= -1
    elif i == 'R':
        ny += 1
    elif i == 'U':
        nx -= 1
    else:
        nx += 1

    if x<=nx<=n and y<=ny<=n:           #영역을 벗어나지 않을 때
        x = nx
        y = ny

    else:                               #영역을 벗어날 때 원래대로 
        nx = x
        ny = y
        continue
print(x,y)


