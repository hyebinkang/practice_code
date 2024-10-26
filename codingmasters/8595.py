n = int(input())
num = list(map(int, input().split()))
tmp = 0
while 2**tmp < len(num):
    tmp +=1

for i in range(2**tmp-len(num)):
    num.append(0)

tree = []
tree.append(num)

while len(num) !=1:
    new = []
    for k in range(0, len(num), 2):
        new.append(num[i]+num[i+1])
    tree.append(new)
    num = new


for i in reversed(tree):
    for j in i:
        print(j, end=' ')
    print()



