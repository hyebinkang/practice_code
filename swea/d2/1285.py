t = int(input())

for i in range(t):
    people = int(input())                               #돌을 던지는 사람의 수

    loc = list(map(int, input().split()))[:people]

    for j in range(people):
        loc[j] = abs(loc[j])                            #0을 기준으로 거리를 따지니까 절댓값으로 바꾸어줌


    print("#{0}".format(i+1), min(loc), loc.count(min(loc)))        #최솟값, 최솟값의 개수를 세어줌