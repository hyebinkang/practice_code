n = int(input())
names = {}

for _ in range(n):
    name, cur = map(str, input().split())
    names[name] = cur

now = []
for name, cur in names.items():
    if cur == 'leave':
        continue
    else:
        now.append(name)
now.sort(reverse=True)
for i in now:
    print(i)