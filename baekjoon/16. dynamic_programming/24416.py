n = int(input())
f = [0 for _ in range(41)]          #미리 0으로 만들어 놓음
cnt_code1 = 0                       #사용 횟수
cnt_code2 = 0

def fib(n):                         #재귀호출 방법
    global cnt_code1                #전역변수로 설정해 준 후 +1을 사용
    cnt_code1 +=1
    if n == 1 or n == 2:            #n이 1과 2일 땐 이용횟수에서 제외
        cnt_code1 -=1
        return 1
    else:
        return fib(n-1)+fib(n-2)    #피보나치 계산

def fibonacci(n):                   #동적 프로그래밍 방법
    global cnt_code2
    cnt_code2 +=1
    f[1],f[2] =1,1                  #1,2는 각각 1과 1
    for i in range(3, n+1):         #3이상일 때
        cnt_code2 +=1
        f[i] = f[i-1]+f[i-2]        #피보나치 계산, 이전 항의 합이 다음 항을 이용
    return f[n]

fib(n)
fibonacci(n)
print(cnt_code1+1, cnt_code2-1)

