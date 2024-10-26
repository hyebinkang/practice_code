n, m, k = map(int, input().split())

num = sorted(list(map(int, input().split())))

first = num[n-1]        #큰 수
second = num[n-2]       #두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m ==0:
            break
        result += first
        m -=1
    if m == 0:
        break
    result += second
    m -=1

print(result)
