import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr_sort = list(sorted(set(arr)))   #arr을 정렬, 중복 제거

dic={arr_sort[i]:i for i in range(len(arr_sort))}   #딕셔너리 형태로 arr_sort의값과 i 저장

for j in arr:                   #arr 안에서 dic의 key값을 찾아준다
    print(dic[j], end = ' ')

