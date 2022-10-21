N, K = map(int, input().split())        #N: 동전 종류 개수, K: 원
cnt = 0                                 #필요한 동전 개수
coin_type=[]                            #동전 종류 리스트
for i in range(N):
    coin_type.append(int(input()))

coin_type.reverse()                     #내림차순으로 정렬

for coin in coin_type:
    cnt += K // coin                    #큰 수 부터 나누어서 몫은 더하기
    K %= coin                           #나머지는 새로운 K
print(cnt)