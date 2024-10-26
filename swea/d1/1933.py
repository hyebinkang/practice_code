n =int(input())

for i in range(1,n+1):
    if n%i == 0:                #약수는 나누면 0이 됨
        print(i, end=' ')