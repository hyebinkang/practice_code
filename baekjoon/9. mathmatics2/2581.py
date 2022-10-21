import sys
m = int(sys.stdin.readline())    #최솟값
n = int(sys.stdin.readline())    #최댓값
prime = []
for i in range(m, n+1): #최솟값 ~ 최댓값 +1
    cnt = 0     #prime개수
    for j in range(2, i+1): #2~i+1까지
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        prime.append(i) #소수 이면 리스트에 추가

if(prime == []):    #리스트에 아무것도 없다면
    print(-1)
else:                   #반대
    print(sum(prime))   #리스트의 합
    print(min(prime))   #리스트 최솟값