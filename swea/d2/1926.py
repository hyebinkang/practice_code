N = int(input())
syk = ['3','6','9']     #3,6,9 일 때 -로 변환
for i in range(1,N+1):
    count = 0               #숫자 안에서 3,6,9의 개수

    for j in str(i):        #문자로 변환한 숫자를 한 문자씩 돌기위함
        if j in syk:
            count +=1

    if count>0:             #0보다 크면 -*count개수 만큼 출력
        print('-'*count, end=' ')
        continue

    print(i, end=' ')       #아니라면 i출력
