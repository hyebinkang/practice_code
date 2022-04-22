import math
import sys
from collections import Counter
n = int(sys.stdin.readline())        #n은 홀수
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

print(round(sum(arr) / len(arr)))       #산술평균

mid = len(arr) // 2
arr_s = sorted(arr)
print(arr_s[mid])                       #중앙값


k=Counter(arr_s).most_common()          #최빈값 
if len(arr_s) > 1:
    if k[0][1] == k[1][1]:print(k[1][0])

    else : print(k[0][0])
else : print(arr_s[0])

print(max(arr)-min(arr))                #범위