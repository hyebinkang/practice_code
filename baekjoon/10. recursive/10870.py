def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)    #피보나치 수열, num-1+num-2를 합한 값을 재귀로 보낸다

num = int(input())
print(fibonacci(num))

# #----for문-----
# n = int(input())
# fn = 0              #0번째 피보나치 수
# fn1 = 1             #1번째 피보나치 수
# fn2= fn+fn1         #0번째 +1번째 수 = 2번째 수(피보나치 수열은 n>=2)
# for i in range(n):
#     fn = fn1
#     fn1 = fn2
#     fn2 = fn+fn1
# print(fn)