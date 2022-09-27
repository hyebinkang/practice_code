t = int(input())

for i in range(t):
    total = 0
    n = int(input())
    for j in range(1,n+1):
        if j%2 == 0:        #j가 짝수이면 -로 변환
            j = -j

        total +=j           #값 더하기

    print('#',i+1, ' ',total, sep='')

