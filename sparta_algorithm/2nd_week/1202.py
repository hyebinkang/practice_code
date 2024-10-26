N,K = map(int, input().split())
jew = {}
for _ in range(N):
    M, V = map(int, input().split())
    jew[M] = V
bag = []
for _ in range(K):
    C = int(input())
    bag.append(C)
bag.sort()

while len(bag)<0:
    for i in range(len(bag)):




