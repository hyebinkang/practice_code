N = str(input())        #숫자를 문자로 입력받기
add = 0                 #자리별 합
for i in N:
    add += int(i)       #문자를 숫자로 변환하여 값 더하기
print(add)
