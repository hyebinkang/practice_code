s = input()                             #소문자 문자열 넣기
alphabet = 'abcdefghijklmnopqrstuvwxyz' #a~z까지

for i in alphabet:
    if i in s:                         #s안에 a~z가 들어 있다면
        print(s.index(i), end=' ')     # 그 자리를 s의 index값으로 표현
    else:
        print(-1, end=' ')              #없다면 -1로 표현