N, M = map(int, input().split())

card = list(map(int, input().split()[:N]))
avg_list=[]

for i in range(len(card)):
    for j in range(len(card)):
        if i == j:
            continue
        for k in range(len(card)):
            if i == k:
                continue
            elif j == k:
                continue
            else:
                if(card[i]+card[j]+card[k] <= M):
                    avg_list.append(card[i]+card[j]+card[k])

print(max(avg_list))
