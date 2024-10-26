n = int(input())
down = []
for _ in range(n):
    arr = list(map(int, input().split()))[:_+1]
    if arr == 1:
        pass
    else:
        now_a = arr.index(max(arr))
        pre_a = now_a
        if arr[now_a+1] >=
        print(a)

    down.append(max(arr))

print(down)
print(sum(down))