t= int(input())

for i in range(t):
    text = str(input())
    if text[0:] == text[::-1]:              #회문: 문자열 거꾸로 읽기[시작:끝:규칙]
        print("#{0}".format(i+1), 1)
    else:
        print("#{0}".format(i+1), 0)