n = int(input())    #n번째 수 입력

cross = 0           #사선 횟수
avg_cross = 0       #사선 안에서 최대의 값을 의미
while n > avg_cross:
    cross +=1           #사선 횟수 +1
    avg_cross += cross  #사선 횟수 + avg_cross = 사선 안에서 최대의 값을 의미하게 된다.

gap = avg_cross - n     #최대의 값에서 -n
if cross % 2 == 0:      #사선이 짝수번째 이면
    x = cross - gap     #분자
    y = gap + 1         #분모
else:
    x = gap +1          #분자
    y = cross -gap      #분모

print(x,'/',y, sep='')  #결과 출력