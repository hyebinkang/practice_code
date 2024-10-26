t= int(input())

for i in range(t):
    n = int(input())
    state = 'No'                        #상태를 미리 지정
    for j in range(1, 10):              #1부터 9까지
        a = n//j                        #몫
        if a*j == n:                    #검토
            if 0<a<10:
                state = 'Yes'           #상태 바꾸기
                break
    print("#{0}".format(i+1), state)    #출력

