t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if a+b == 24:
        print("#{0}".format(i+1), 0)            #24시는 0시로 표현
    elif a+b > 24:
        print("#{0}".format(i+1), a+b-24)       #24가 넘어가면 -24
    else:
        print("#{0}".format(i + 1), a+b)        #24가 넘어가지 않는 경우
