t = int(input())


for _ in range(t):
    num = int(input())
    arr = [][:num]
    arr_90 = [[0]*num]*num
    arr_180 = [[0] * num] * num
    arr_270 = [[0] * num] * num

    for i in range(num):
        arr.append(list(map(int, input().split())))

    for i in range(num):
        for j in range(num):
            arr_90[i][j] = arr[num-j-1][i]

    for i in range(num):
        for j in range(num):
            arr_180[i][j] = arr[num-i-1][num-j-1]

    for i in range(num):
        for j in range(num):
            arr_270[i][j] = arr[j][num-i-1]


    for i in range(num):
        for a in range(num):
            print(arr_90[i][a], end='')