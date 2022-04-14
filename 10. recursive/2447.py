N, M = map(int, input().split())            #N: 카드의 개수, M: M을 넘지 않으면서 최대한 가까운 수

card = list(map(int, input().split()[:N]))  #리스트로 카드입력 받기
avg_list=[]                                 #3수의 합을 더할 때 저장

for i in range(len(card)):                  #첫번째 카드 고르기
    for j in range(len(card)):              #두번째 카드
        if i == j:                          #단, 첫번째 카드와 두번째 카드의 순서가 같다면 continue
            continue
        for k in range(len(card)):          #세번째 카드
            if i == k:                      #첫번째 카드와 순서가 같으면 continue
                continue
            elif j == k:                    #두번째 카드와 순서가 같으면 continue
                continue
            else:
                if(card[i]+card[j]+card[k] <= M):       #card의 합이 M이하 일 때 리스트에 저장
                    avg_list.append(card[i]+card[j]+card[k])

print(max(avg_list))#최댓값 출력
