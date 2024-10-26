t = int(input())

num = [0,1,2,3,4,5,6,7,8,9]     #0~9

def double(z):                      #z=n*cnt
    while num != count:
        while z // 10 != 0:         #한 자리 수 이상 일 때
            count[z%10] = z%10      #10으로 나눈 나머지를 인덱스 값으로 설정 = 나머지 숫자로 바꿈
            z //= 10                #z는 몫이 됨
        if z // 10 == 0:            #한 자리 수 일 때
            count[z%10] = z%10
        break

for i in range(t):
    n = int(input())
    cnt = 0                             #횟수
    count =[1,0,0,0,0,0,0,0,0,0]       #1은 숫자 0을 대신, 들어올 숫자들의 자리를 만들어 둠

    while True:
        if num != count:                #두 리스트가 같아질 때 까지
            cnt += 1                    # 횟수 늘려가기
            double(n*cnt)

        else:
            break

    print("#{0}".format(i+1), n*cnt)

