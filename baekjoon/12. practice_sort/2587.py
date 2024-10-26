number = []

for _ in range(5):
    number.append(int(input()))

number.sort()                           #모든 인자를 받은 상태에서 정렬해야 함
print(sum(number)//len(number))         #평균값
print(number[2])                        #중앙값
