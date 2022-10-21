def factorial(num):
    if num != 0:
        return factorial(num-1) * num       #재귀함수 부분, num이 -1씩 줄어들고 곱을 반환
    else:
        return 1                            #0일 때 1반환
num = int(input())
print(factorial(num))                       #결과 출력


# #---for문----
# n = int(input())
# result = 1
# for i in range(1, n+1):
#     result *=i              #result 에 1부터 곱하기
#     print(result)