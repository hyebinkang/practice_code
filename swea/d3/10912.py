t= int(input())

for _ in range(t):
    line = input()  2번 반복되는 문자들은 삭제하고 남은 문자만 출력하기
    letter = []                     #각각 문자 넣는 리스트
    for i in line:
        if not letter:              #1글자도 없다면 넣고
            letter.append(i)
        elif i in letter:           #같은 글자가 있다면 삭제
            letter.remove(i)
        else:                       #글자가 있지만 같지 않을 때 넣기
            letter.append(i)

    letter.sort()                   #정렬
    if not letter:
            print("#{0}".format(_+1), "Good")       #아무것도 없다면
    else:
        print("#{0}".format(_+1), end=' ')          #있다면 횟수 먼저 출력 후
        for j in letter:
            print(j, end='')                        #문자 각각 출력
            print()