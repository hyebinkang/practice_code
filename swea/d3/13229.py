t= int(input())

S = ["MON", "TUE", "WED", "THU", "FRI", "SAT","SUN"]        #요일


for _ in range(t):
    day = input()                                           #요일 입력
    if day in S:
        result = S.index(S[-1]) - S.index(day)              #마지막 인덱스 = SUN, 입력받은 요일 index 값 빼기
        if result == 0:                                     #입력받은 요일이 SUN이면 7
            result = 7

    print("#{0} {1}".format(_+1, result))