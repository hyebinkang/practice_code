m, n = map(int, input().split())

a = [[0 for i in range(n)] for i in range(m)]       #n,m구분 n은 행, m은 열


for _ in range(2):
    for j in range(m):
        num = list(map(int, input().split()))       #행렬에 입력할 것을 리스트로 받음
        for k in range(n):
            a[j][k] += num[k]                       #위치마다 리스트의 수를 더해준다

for _ in a:
    for e in _:
        print(e, end=' ')                           #출력
    print()