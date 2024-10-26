t = int(input())
sudoku = [1,2,3,4,5,6,7,8,9]


for _ in range(t):
    puzzle = []             #가로 줄 기준 숫자 입력
    line = []               #세로 줄 평가
    result = 1              #제대로된 스도쿠인지 결과

    for i in range(9):
        puzzle.append(list(map(int, input().split())))

    while result == 1:                          #result = 0일때 바로 종료
        for j in puzzle:                        #가로 줄 평가
            if sorted(j) == sudoku:
                continue
            else:
                result = 0
                break

        for k in range(9):              #가로         #세로줄 평가
            for l in range(9):          #세로
                if puzzle[l][k] in sudoku:
                    line.append(puzzle[l][k])

                    if l == 8:
                        if sorted(line) != sudoku:
                            result = 0
                            break
                        else:
                            line = []

        for m in range(0,9,3):                  #3*3평가, (출발, 도착, 건너뛰기)
            if m == 3 or m ==6:                 #시작점을 기준
                if sorted(line) !=sudoku:
                    result = 0
                    break

            for n in range(0,9,3):
                line = []

                for squ_w in range(3):
                    for squ_h in range(3):
                        if puzzle[squ_w+m][squ_h+m] in sudoku:
                            line.append(puzzle[squ_w+m][squ_h+m])
        break                                                        #모두 통과 했을 때 종료

    print("#{0} {1}".format(_+1, result))