import sys
n = int(sys.stdin.readline())

arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x,y))               #x,y를 하나의 인자로 입력

arr.sort()                          #정렬

for j in range(n):
    print(arr[j][0], arr[j][1])     #x가 같은 숫자일 때, y가 작은 것 부터 print