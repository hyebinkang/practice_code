t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    result = 0
    line = []

    for i in range(N):
        line.append(list(map(int, input().split())))        #이중 리스트로 만들기

    for j in range(N-M+1):              #N-M+1 파리채를 칠 수 있는 공간의 범위
        for k in range(N-M+1):
            fly = 0
            for l in range(M):              #M번만큼 실행
                for a in range(M):
                    fly +=line[j+l][k+a]    #M*M사이즈 안에 있는 것을 전체 다 돌 수 있음

            if fly >= result:
                result = fly                #result랑 비교하여 큰 값을 result로
            else:
                continue

    print("#{0}".format(_+1), result)