#스택 예제---------------------------
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])  #최상단 원소 부터 출력

#큐 예제---------------------------
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()         #가장 먼저 들어온  원소 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(deque)
queue.reverse()
print(queue)


#재귀 함수 예제---------------------------
def recursive_function():
    print("재귀 함수 호출")
    recursive_function()

recursive_function()

#재귀 함수 종료 예제---------------------------
def recursive_function(i):
    if i == 100:
        return print(i, '번째 재귀함수에서', i+1, '번째 재귀함수 호출')
        recursive_function(i+1)
        print(i, '번째 재귀 함수를 종료합니다')
recursive_function(1)

