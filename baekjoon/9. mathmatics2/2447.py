# import sys
# k = int(sys.stdin.readline())
# hexagon = []
# right = []
# up = []
#
# for _ in range(6):
#     direction, meter = list(map(int, sys.stdin.readline().split()))
#     hexagon.append([direction, meter])
#
# for i in range(len(hexagon)):
#     for j in range(1):
#         if hexagon[i][0] == 1:
#             right.append(hexagon[i][1])
#
#         elif hexagon[i][0] == 2:
#             right.append(hexagon[i][1])
#
#         elif hexagon[i][0] == 3:
#             up.append(hexagon[i][1])
#
#         elif hexagon[i][0] == 4:
#             up.append(hexagon[i][1])
#
# print(right, up)
# print((max(right)*max(up)-min(right)*min(up))*k)
#------정답코드------
k = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

w = 0
w_idx = 0
h = 0
h_idx = 0

for i in range(len(arr)):
    if arr[i][0]==1 or arr[i][0] == 2:
        if w <arr[i][1]:
            w = arr[i][1]
            w_idx = i
    elif arr[i][0] == 3 or arr[i][0]==4:
        if h <arr[i][1]:
            h = arr[i][1]
            h_idx = i

subW = abs(arr[(w_idx - 1) %6][1] - arr[(w_idx +1)%6][1])
subH = abs(arr[(h_idx -1) %6][1] - arr[(h_idx+1) %6][1])

ans = (((w*h) - (subW*subH)) * k)
print(ans)