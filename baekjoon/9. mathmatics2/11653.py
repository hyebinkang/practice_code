n = int(input())
for j in range(2, n+1): #2부터 n+1까지
    while n != 1:   #n이 1이 아닐 때(=1이 될때 까지, 계속 나누어 떨어질 때 까지)
        if(n % j == 0): #나머지가 0이면
            n = n // j  #n은 n 나누기 j의 몫
            print(j)    #j출력
        else:
            break
#--------시간초과-----------
# n = int(input())
# prime = []
# for i in range(1, n+1):
#     cnt = 0
#     if(n == 1):
#         break
#     for j in range(2, i+1):
#         if(i%j == 0):
#             cnt +=1
#     if(cnt == 1):
#         prime.append(i)           #소수 구하는 코드
#
# for j in prime:                   #구한 소수 안에서 다시 for문
#     while n != 1:
#         if(n % j == 0):
#             n = n // j
#             print(j)
#         else:
#             break


