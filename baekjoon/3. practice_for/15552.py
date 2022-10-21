import sys

t= int(input())

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

#빠르게 a+b하는 방법, sys사용