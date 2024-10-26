t= int(input())

for i in range(t):
    a,b = map(int, input().split())                 #두 수를 입력
    print('#',i+1, ' ', a//b,' ', a%b, sep='')      #몫과 나머지 출력하기