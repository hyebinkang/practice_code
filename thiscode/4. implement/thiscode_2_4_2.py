N = int(input())

count = 0

for i in range(N+1):                                #시간 N+1시간 전까지
    for minutes in range(60):                       #분
        for seconds in range(60):                   #초
            if '3' in str(i)+str(minutes)+str(seconds):         #문자열에 3이 포함되어 있으면
                count +=1
print(count)