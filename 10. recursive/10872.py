def factorial(num):
    if num != 0:
        return factorial(num-1) * num       #재귀함수 부분, num이 -1씩 줄어들고 곱을 반환
    else:
        return 1                            #0일 때 1반환
num = int(input())
print(factorial(num))                       #결과 출력