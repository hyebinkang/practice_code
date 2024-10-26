t = int(input())

for i in range(t):
    n = int(input())
    for j in range(2, n+1):
        if n//j == 0:
            print("possible")
            break
        else:
            continue
