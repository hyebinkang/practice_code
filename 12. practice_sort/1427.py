num = []
n = input()             #n을 문자로 받고

for i in n:
    num.append(int(i))      # 한 글자씩 num에 넣어준다
num.sort(reverse=True)      #내림차순

for j in num:               #엔터 없이 내림차순으로 출력
    print(j, end='')







