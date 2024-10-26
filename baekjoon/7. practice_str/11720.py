n = int(input())    #숫자 n개자리 수 입력
s = input()         #n개 자리를 문자열로 받음
sum_s = 0           #합
for i in s:         #문자열을 for문으로 돌림 이 때, range는 쓰지 않음
    sum_s += int(i) #문자열을 int로 한자리씩 더해줌
print(sum_s)


