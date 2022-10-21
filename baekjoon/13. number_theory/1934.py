n = int(input())

for i in range(1, n+1):
    arr = []                            #리스트 초기화
    a,b = map(int, input().split())

    for j in range(1, min(a,b)+1):
        if(a%j == 0 and b%j==0):        #a와 b가 둘다 나누어 떨어져야 함
            arr.append(j)               #해당하는 수 저장

    print(max(arr)*a//max(arr)*b//max(arr)) #최대공약수로 각 a,b를 나눈 것의 몫을 곱하면 최소공배수가 된다.