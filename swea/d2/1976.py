t = int(input())

for i in range(t):
    h, m, h1, m1 = map(int, input().split())        #시, 분 입력
    new_h = h + h1          #더하는 시간
    new_m = m + m1          #더하는 분

    if new_m >=60:          #60이 넘어가면 1시 추가
        new_h += 1
        new_m -= 60
    if new_h >=13:          #12시간 기준
        new_h -=12

    print("#{0}".format(i+1), new_h, new_m, sep=' ')