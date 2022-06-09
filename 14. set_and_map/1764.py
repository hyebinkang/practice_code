n, m = map(int, input().split())
arr = {}
union = list()
for _ in range(n):
    s = input()
    arr[s] = True

for i in range(m):
    a = input()
    if a in arr.keys():
        union.append(a)

new_union = sorted(union)
print(len(union))
for j in new_union:
    print(j)