import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))[:N]
arr = [0]
temp = 0

for a in num:

    temp += a
    arr.append(temp)

for _ in range(M):

    i, j = map(int, sys.stdin.readline().split())
    print(arr[j]-arr[i-1])