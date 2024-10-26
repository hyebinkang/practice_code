t = int(input())

for _ in range(t):
    num = int(input())
    arr = [][:num]
    arr_90 = [[0 for _ in range(num)] for _ in range(num)]              #0과 리스트를 개별적으로 만들어줘야 함 -> for문을 사용한 이유
    arr_180 = [[0 for _ in range(num)] for _ in range(num)]
    arr_270 = [[0 for _ in range(num)] for _ in range(num)]


    for i in range(num):
        arr.append(list(map(int, input().split())))

    for i in range(num):
        for j in range(num):
            arr_90[i][j] = arr[num-j-1][i]                          #90도를 회전 시켰을 때

    for i in range(num):
        for j in range(num):
            arr_180[i][j] = arr[num-i-1][num-j-1]                   #180도 회전

    for i in range(num):
        for j in range(num):
            arr_270[i][j] = arr[j][num-i-1]                         #270도 회전

    print("#{0}".format(_+1))
    for i in range(num):
        for a in range(num):
            print(arr_90[i][a], end='')                            #90도, 180도, 270도 차례대로 회전
        print(end=' ')                                             #띄우기
        for b in range(num):
            print(arr_180[i][b], end='')
        print(end=' ')
        for c in range(num):
            print(arr_270[i][c], end='')
        print()                                                     #개행