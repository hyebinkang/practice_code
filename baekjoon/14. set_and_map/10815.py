import sys
M = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split()))       #가지고 있는 숫자 카드 집합
                                                        #있고 없음을 따지는 문제이므로 set을 사용할 수 있음
N = int(input())
note_arr = list(map(int, sys.stdin.readline().split())) #적혀져 있는 정수

for i in range(N):              #적혀진 수 대로 있고, 없음을 출력 즉, 범위가 range(N)
    if note_arr[i] in arr:      #적혀져 있는 정수 i번째가 arr에 있다면
        print(1, end=' ')       #1출력
    else:
        print(0, end=' ')       #없으면 0 출력