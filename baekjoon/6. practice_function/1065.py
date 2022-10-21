#한수: 연속된 두 개의 수가 일정한 수열
def han_num(n):
    han_list = []   #한수를 넣을 리스트

    for i in range(1,n+1): #n만큼 for문 실행
        n_hun = i // 100    #백의 자리
        n_ten = i % 100 // 10   #십의 자 리
        n_one = i % 100 % 10    #일의 자리

        if (n_hun == 0):    #한자리 수와 두자리 수는 모두 한수에 속한다(1~9: 길이가 1인 등차수열 | 10~99: 공차가 1개 밖에 없으므로 등차수열)
            han_list.append(i)
        else:
            if(n_hun - n_ten == n_ten - n_one): #3자리 수인 숫자들이 한수가 되기 위한 조건, 공차(공통으로 나타나는 차)의 기준
                han_list.append(i)
    print(len(han_list))    #리스트의 길이를 보여줌
    return han_list         #리스트 반환

n = int(input())            #n을 입력할 수 있도록 만들어줘야 함
han_num(n)