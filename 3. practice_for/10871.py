n,x = map(int, input().split())#공백으로 숫자 구분 삽입
a = list(map(int, input().split()))
for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")
#n개의 수 중 x보다 작은 수 출력
#a 는 리스트, 모두 다 다른 수