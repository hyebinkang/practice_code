n = int(input())
first = 666
cnt = 0

while True:
    if '666' in str(first):         #666이란 문자가 first안에 있다면
        cnt += 1                    # +1
    if cnt == n:                    #cnt와 n이 같다면 종료
        print(first)
        break
    first +=1                       #모두 아닐 경우 first에 1씩 증가시켜 first가 666을 포함하는 수로 만들어줘야 함
