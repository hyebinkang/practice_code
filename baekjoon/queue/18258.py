import sys
from collections import deque                       #큐 사용 할 때 임포트

data = deque()                                      #큐 선언 deque([])
input = sys.stdin.readline
n = int(input())

for i in range(n):
    order = list(map(str, input().split()))

    if order[0] == 'push':
        data.append(order[1])                       #큐 삽입
    elif order[0] == 'pop':
        if len(data) == 0:
            print(-1)
        else:
            print(data.popleft())                   #맨 앞 인자 pop
    elif order[0] == 'size':
        print(len(data))
    elif order[0] == 'empty':
        if not data:                                #안에 아무것도 없다면
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not data:
            print(-1)
        else:
            print(data[0])
    else:
        if not data:
            print(-1)
        else:
            print(data[-1])
