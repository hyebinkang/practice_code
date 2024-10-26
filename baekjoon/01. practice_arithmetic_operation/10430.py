a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print((a%c) * (b%c)%c)
#map 함수 사용시 동시에 2개 이상의 인자 입력 가능
