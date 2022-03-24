a,b = map(int, input().split()) #공백 기준으로 두 수 입력 받기
while a+b != 0: #계속 반복
    print(a+b)
    a,b = map(int, input().split())
    if a+b == 0:    #a,b가 0이면 종료
        break
