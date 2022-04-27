import sys
n = int(sys.stdin.readline())

arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((y,x))               #y,x 순으로 입력

arr.sort()                          #정렬

for j in range(n):
    print(arr[j][1], arr[j][0])     #y,x반대로 출력