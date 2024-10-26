num = [[0 for i in range(9)] for i in range(9)]     #행열
big = 0                                             #가장 큰 수
cols = 0                                            #큰 수의 열
rows = 0                                            #큰 수의 행
for row in range(9):
    line = list(map(int, input().split()))
    if big < max(line):                             #입력 받은 리스트에서 가장 큰 수와 비교
        big = max(line)                             #크다면 big은 새로운 값
        rows = row                                  #행 = for문의 row값
        cols = line.index(max(line))                #열 = 큰 수의 인덱스 값

    for col in range(9):
        num[row][col] = line[col]                   #행렬에 인자 넣기

print(big)
print(rows+1, cols+1)