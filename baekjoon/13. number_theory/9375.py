n = int(input())                    #가진 의상의 수

for _ in range(n):
    k = int(input())                #k개의 의상의 이름과 종류 입력받기
    cloth = {}                      #딕셔너리로 받기
    for i in range(k):
        name, kind = input().split()

        if kind in cloth.keys():        #딕셔너리의 key중 kind와 같은 것이 있다면
            cloth[kind].append(name)    #kind의 value값에 name을 저장
        else:
            cloth[kind] = [name, ""]    #없다면 'kind': [이름,''] 의 형식으로 저장

    answer = 1                          #answer초기값 1
    for key in cloth.keys():            #cloth의 key를 가지고 온다
        answer *= len(cloth[key])       #key에 저장된 cloth[key]의 value값 을 answer에 곱하여 개수 구하기

    print(answer-1)                     #아무것도 입지 않은 경우를 제외해 준다.
