t = int(input())

for i in range(t):
    a,b = map(int, input().split())

    if a >= 10 or b >=10:                       #둘 중 하나라도 10이 넘는다면
        print("#{0}".format(i+1), -1)           #-1 출력
    else:
        print("#{0}".format(i + 1), a*b)        #아니라면 a*b 출력