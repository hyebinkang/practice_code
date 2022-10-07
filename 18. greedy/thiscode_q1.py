N = int(input())

afraid = sorted(list(map(int, input().split())))[:N]

group = 0
people = 0

for i in afraid:
    people +=1                      #사람 수 먼저 증가
    if people >= i:                 #사람 수가 i보다 크면 그룹 생성
        group+=1
        people=0                    #그룹 +1, 사람수 0
print(group)
