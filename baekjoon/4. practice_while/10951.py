while True: #while 1과 같은 의미
    try:
        a,b = map(int, input().split()) #a,b입력
        print(a+b)
    except: #a,b입력이 되지 않을 경우 break
        break

#try문에 실행코드를, except문에 예외처리 코드를 작성