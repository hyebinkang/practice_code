h = 23
m = 59
s = 59

n = int(input())
cnt = 0
for i in range(h+1):
    for j in range(m+1):
        for k in range(s+1):
            num = f"{str(i)}:{str(j)}:{str(k)}"
            if str(n) in num:
                cnt += 1

print(cnt)
