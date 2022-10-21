n = int(input())
num = []
for i in range(n):
    num.append(int(input()))        #숫자 입력
    num.sort()                      #정렬

for _ in num:                       #출력
    print(_)