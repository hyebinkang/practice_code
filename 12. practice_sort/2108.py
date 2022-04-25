import math
import sys
from collections import Counter
n = int(sys.stdin.readline())        #n은 홀수
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

print(round(sum(arr) / len(arr)))       #산술평균,   전체의 합/arr의 길이

mid = len(arr) // 2
arr_s = sorted(arr)
print(arr_s[mid])                       #중앙값, 길이를 나누기 2를 한 몫을 인덱스로 받으면 중앙값


k=Counter(arr_s).most_common()          #최빈값, 카운팅 하여 개수 많은 순으로 딕셔너리 형태의 반환
if len(arr_s) > 1:
    if k[0][1] == k[1][1]:print(k[1][0])    #람다식을 이용하여 출력

    else : print(k[0][0])
else : print(arr_s[0])

print(max(arr)-min(arr))                #범위, 최댓값에서 최솟값을 빼면 범위