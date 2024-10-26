n = int(input())
queue = []
for i in range(n):
    order = list(map(str, input().split()))
    o = order[0]
    if o == 'push':
        queue.append(int(order[1]))
    elif o == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif o == 'size':
        print(len(queue))
    elif o == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif o == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif o == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
