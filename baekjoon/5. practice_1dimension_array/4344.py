c = int(input())    #테스트 케이스의 개수

for i in range(c):
    avg = 0 #각 테스트 별로 총합이라서 초기화 시켜줘야 함
    score_avg = 0   #각 테스트 별 평균
    ratio = 0   #평균보다 높은 점수 비율
    score_list = [] #테스트 케이스 리스트

    score_list = list(map(int, input().split()))    #n명의 사람과 점수 입력
    num = score_list[0] #첫번째에 입력하는 사람 수가 num
    score_list.remove(num)  #리스트에서 제거 score_list[1:] 제거 하지 않고도 이런 식으로 쓸 수 있음

    for j in range(num):
        avg += score_list[j]    #총합 구하는 식

    score_avg += avg / num  #평균

    for k in range(len(score_list)):    #비율 구하는 방법, 리스트의 수를 범위로 설정
        if(score_list[k] > score_avg):  #평균보다 높은 점수 일 때 +1
            ratio += 1

    ratio_score = ratio/num * 100   #백분위로 비율 구하기

    print(f"{format(ratio_score, '.3f')}%") #format을 사용하여 숫자 자리수를 맞춰줘야 함 f"{format(숫자, 자리수'n.f')}%"이렇게