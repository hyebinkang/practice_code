from math import gcd                #최대공약수 구하는 함수
n = int(input())
arr = list(map(int, input().split()))[:n]

for i in range(n-1):                #arr[0]은 기준이 될 숫자이므로 제외, n-1까지 계산
    num = gcd(arr[0], arr[i+1])     #최대공약수를 구함

    print(arr[0]//num,'/',arr[i+1]//num, sep='')    #sep로 공백 제거
