while True:
    num = list(map(int, input().split()))       #리스트로 숫자 저장
    num.sort()                                  # 오름차순일 때만 식이 성립하기 때문에 오름차순 배열
    if sum(num) == 0:                           #숫자의 합이 0이면 전체가 0
        False
        break
    else:
        if((num[0]**2 + num[1]**2)**0.5 == (num[2]**2)**0.5):       #x의 제곱 + y의 제곱 은 z제곱의 루트값과 같다
            print("right")
        else:
            print("wrong")