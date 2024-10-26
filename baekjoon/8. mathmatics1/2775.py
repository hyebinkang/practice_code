t = int(input())
total = 0
for i in range(t):
    k = int(input())    #층
    n = int(input())    #호
    people = [_ for _ in range(1, n+1)] #k-1층 까지 n호 사람의 합
    for j in range(k):
        for l in range(1,n):
            people[l] += people[l-1]    #각 호실 사람의 수를 합함
    print(people[-1])   #가장 마지막 수 = n호 합

