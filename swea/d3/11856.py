t = int(input())

for _ in range(t):
    line = set(input())                     #set으로 받기 = 중복 제거
    if len(line) == 2:                      #길이가 2라면 조건에 맞게 중복이 되는 것
        print("#{0}".format(_+1), 'Yes')
    else:
        print("#{0}".format(_+1), 'No')