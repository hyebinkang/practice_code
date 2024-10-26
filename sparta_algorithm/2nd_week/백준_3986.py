N = int(input())
result = 0
for i in range(N):
    word = input()
    stack = []
    for j in word:
        if len(stack) == 0:
            stack.append(j)
        elif stack[-1] == j:
            stack.pop()
        else:
            stack.append(j)
    if len(stack) == 0:
        result +=1
print(result)