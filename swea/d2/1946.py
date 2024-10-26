t= int(input())

for i in range(t):
    alphabet = []                               #알파벳 넣을 리스트
    n = int(input())                            #테스트 케이스
    for _ in range(n):
        eng, num = map(str, input().split())
        alphabet.append(eng*int(num))           #문자를 숫자만큼 곱해서 리스트 저장

    alphabet = ''.join(alphabet)                #''로 문자열 합침
    cnt = 0

    print("#{0}".format(i+1))                   #횟수 출력
    for j in alphabet:
        for k in j:
            cnt +=1
            if cnt == 10:                       #cnt가 10이면 개행
                print(k)
                cnt = 0
            else:
                print(k, end='')                #10이 아니면 개행 x
    print()