N,M = map(int, input().split())
board = []
index_list = []
for i in range(N):
    board.append(input())

for j in range(N-7):                    #8*8의 보드판이 되어야 하므로, 0~7까지 가로범위
    for k in range(M-7):                #세로 범위
        index1 = 0                      #1번째의 경우
        index2 = 0                      #2번째의 경우
        for a in range(j, j+8):         #8*8씩 한 단어씩 보는 코드, 가로
            for b in range(k, k+8):     #세로
                if(a+b) % 2 == 0:
                    if board[a][b]!='W':    #ex)0,0이 w가 아니면 1증가
                        index1 +=1
                    elif board[a][b]!='B':
                        index2 +=1

                else:
                    if board[a][b]!='B':
                        index1 += 1
                    elif board[a][b]!='W':
                        index2 +=1
        index_list.append(index1)
        index_list.append(index2)

print(min(index_list))  #최솟값 출력


