t = int(input())

money = [50000,10000,5000,1000,500,100,50,10]       #돈 종류

for i in range(t):
    n = int(input())
    print("#", i + 1, sep='')

    for j in money:
        print(n // j, end=' ')                      #money로 n나누기
        n %= j                                      #n은 j로 나눈 나머지
    print()

