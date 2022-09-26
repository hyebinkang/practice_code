a,b = map(int, input().split())

if a == 1:      #비기는 경우 없는 가위바위보 모든 경우의 수
    if b == 2:
        print('B')
    else:
        print('A')
elif a==2:
    if b == 3:
        print('B')
    else:
        print('A')
else:
    if b==1:
        print('B')
    else:
        print('A')