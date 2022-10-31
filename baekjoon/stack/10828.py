import sys
input = sys.stdin.readline
n = int(input())

stack = []          #스택에 사용할 리스트

for _ in range(n):
    order = list(map(str, input().split()))         #입력 받는 것을 리스트로 만들어줌

    if order[0] == 'push':
        stack.append(int(order[1]))                 #리스트 안 문자와 숫자 분리하여 넣기

    elif order[0] == 'pop':
        if not stack:                               #stack이 비어있으면, stack ==[]
            print(-1)
        else:
            print(stack.pop())                      #pop명령어를 실행하며, 해당 숫자 보여주기
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] =='empty':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])                        #스택의 가장 마지막 것을 출력
