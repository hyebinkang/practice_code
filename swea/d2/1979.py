t= int(input())

for _ in range(t):
    n, k = map(int, input().split())
    puzzle =[]
    result = 0

    for i in range(n):
        puzzle.append(list(map(int, input().split())))

    for rows in puzzle:
        if rows.count(1) == k:
            result += 1
            continue
        for row in range(n):
           if rows[row]== 1:
               if rows[row+1] and rows[row+2] == 1:
                   if rows[row+3] == 0:
                       result +=1


    print(result)