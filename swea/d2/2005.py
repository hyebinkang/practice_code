t = int(input())

for i in range(t):

    N = int(input())
    line = [[1]][:N]


    for j in range(1, N):
        for k in range(1,N):
            try:
                num = line[j][k]+line[j][k+1]
            except:
                line.append([line[j][0]])
    print(line)
