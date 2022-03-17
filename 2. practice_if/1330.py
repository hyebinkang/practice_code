a, b = map(int, input().split())    #공백을 기준으로 두 수 입력받기
if a>b:
    print('>')
elif a<b:
    print('<')
else: print('==')