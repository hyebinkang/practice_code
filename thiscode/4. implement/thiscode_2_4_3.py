input_data = input()
row = int(input_data[1])                            #가로
column = int(ord(input_data[0])) - int(ord('a'))+1  #세로

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]   #나이트가 이동할 수 있는 범위

result = 0
for step in steps:
    next_row = row+step[0]          #가로 이동
    next_column = column+step[1]    #세로 이동

    if 1<=next_row<=8 and 1<=next_column<=8:    #범위에 들어오면
        result +=1
print(result)