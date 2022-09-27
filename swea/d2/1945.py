n_list = [2,3,5,7,11]       #소수 리스트

t = int(input())

def squ(n):                         #재귀함수 사용
    if n != 1:
        for i in range(5):
            if n % n_list[i] == 0:
                t_list[i] +=1               #해당 인덱스 값에 맞춰 +1
                if n // n_list[i] !=1:      #1이 아니면
                    squ(n // n_list[i])     #다음 수
                break                       #아니라면 break
            else:
                continue

for i in range(t):
    t_list = [0, 0, 0, 0, 0]
    n = int(input())
    squ(n)
    print("#{0} {1} {2} {3} {4} {5}".format(i+1, t_list[0], t_list[1], t_list[2], t_list[3], t_list[4]))        #정해진 format형태로 출력

