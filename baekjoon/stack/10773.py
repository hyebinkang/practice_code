k = int(input())
arr = []
for i in range(k):
    num = int(input())

    if num == 0:
        arr.pop()           #pop은 가장 최근에 들어온 수를 지우기 때문에 인자를 쓸 필요가 없음
    else:
        arr.append(num)

print(sum(arr))