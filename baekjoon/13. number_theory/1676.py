import math

a = math.factorial(int(input()))        #input값의 팩토리얼 값
count = 0                               #뒤에서 부터 0의 개수 count
a_list = []                             #각 숫자를 리스트로
while a != 0:                           #a를 리스트로 넣는 과정
    num = a_list.append(a%10)
    new_a = a//10
    a= new_a

for i in a_list:                        #리스트에서 0일 때 +1, 0이 아닌 것이 나오면 종료
    if i == 0:
        count +=1
    else:
        break

print(count)