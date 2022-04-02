# 시간초과
# m, n = map(int, input().split())
#
# for i in range(m, n):     #범위 내에서 for문
#     cnt = 0
#     for j in range(2, i+1):   #2~ i+1범위까지
#         if(i % j == 0):       #나머지가 0이면
#             cnt +=1           #추가
#     if(cnt == 1):             #1이면 소수 출력
#         print(i)

#에라토스테네스의 체
m,n = map(int, input().split())
array = []

for i in range(m, n+1):
    prime = True    #bool타입 선언
    if i ==1:
        continue    #continue: 바로 다음 순번 진행(1 불포함), pass: 이번 행동을 하고 다음 순번 진행(1포함)
    for j in range(2, int(i**0.5) +1):  #0.5는 제곱근을 의미, sqrt(i)와 같은 의미
        if i % j ==0:
            prime = False       #나머지가 0이면 False선언
            break
    if prime == True:           #if prime: 도 같은 의미
        array.append(i)
        print(i)



# #함수 사용
# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True           #소수인 것들에 True반환
# M,N = map(int, input().split())
#
# for i in range(M, N+1):
#     if isPrime(i):    # i하나만 함수에 넣기
#         print(i)
