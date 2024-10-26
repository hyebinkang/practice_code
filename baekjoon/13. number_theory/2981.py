# import sys
# n = int(sys.stdin.readline())
# arr = []
# result = []
# rest= []
#
# for _ in range(n):
#     arr.append(int(sys.stdin.readline()))
#
# arr = sorted(arr)
#
# def paper():
#     for i in range(2, max(arr)):
#         for j in range(n):
#             rest.append(arr[j] % i)
#
#         if len(set(rest)) == 1:
#             result.append(i)
#         rest.clear()
#
# paper()
#
# for p in result:
#     print(p, end=' ')

import math
import sys
n = int(sys.stdin.readline())
arr = []
result = []
rest= []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

def paper():
    for i in range(2, max(arr)):
        for j in range(n):
            rest.append(arr[j] % i)

        if len(set(rest)) == 1:
            result.append(i)
        rest.clear()

paper()

for p in result:
    print(p, end=' ')