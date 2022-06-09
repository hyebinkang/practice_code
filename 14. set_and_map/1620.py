import sys

n, m = map(int, sys.stdin.readline().split())
arr = {}

for _ in range(n):
    put = sys.stdin.readline().strip()
    arr[put] = _

arr_keys = list(arr.keys())

for i in range(m):
    answer = sys.stdin.readline().strip()
    if answer.isdigit():
        print(arr_keys[int(answer)-1])
    else:
        print(arr[answer]+1)