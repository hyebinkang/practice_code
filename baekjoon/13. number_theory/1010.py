import math
t = int(input())

for _ in range(t):
    N, M = map(int, input().split())    #강의 서쪽 N, 강의 동쪽 M (N<=M), M: 원소의 개수, N: 부분집합 경우의 수
    bridge = math.factorial(M)//(math.factorial(N)*math.factorial(M-N))     #조합공식 = 이항계수 공식
    print(bridge)