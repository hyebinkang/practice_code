n = int(input())

for i in range(n):
    vps = []
    stack = input()

    for k in stack:
        if k == '(':
            vps.append(k)
        else:
            if len(vps) ==0:
                vps.append(k)
                break
            vps.pop()

    if not vps:
        print('YES')
    else:
        print('NO')