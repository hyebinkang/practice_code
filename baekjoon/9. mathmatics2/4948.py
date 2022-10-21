import sys
def isPrime(num):
    if num == 1:            #1은 소수가 아님
        return False
    else:
        for i in range(2, int(num**0.5)+1): #2부터 num의 제곱근 +1의 범위까지
            if num%i == 0:
                return False        #소수가 아닌 것들

        return True           #소수인 것들에 True반환

number = [_ for _ in range(2, 123456*2+1)]      #범위가 1<=n<=123,456이기 때문에 미리 설정
prime = []
for x in number:                    #소수 인 것들만 먼저 뽑아놓음
    if isPrime(x):
        prime.append(x)


while True:
    M = int(sys.stdin.readline())           #M 입력받기
    array = []

    if M == 0:
        break       #0일 경우 break

    for i in prime:     #미리 뽑아놓은 소수 범위 안에서
        if M < i <= 2*M:    #범위 안에 해당하는 것을 array에 저장
            array.append(i)
    print(len(array))   #개수 출력

# #------시간초과------
#
# import sys
# def isPrime(num):
#     if num == 1:
#         return False
#     elif num !=1:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         array.append(num)       #array에 저장
#         return True           #소수인 것들에 True반환
#
# while True:
#     M = int(sys.stdin.readline())
#     array = []
#     if M == 0:
#         break
#
#     for i in range(M+1, M*2+1):     #range범위에서 시간 초과가 일어남
#         isPrime(i)
#     print(len(array))
#
#
