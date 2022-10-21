num = int(input())  #몇 개를 입력할 것인지

for i in range(num):
    result = list(str(input())) #문자열 리스트로 받을 때 append사용하기 보다는 지역변수로 만들어줌
    score = 0   #score 점수 계산, 한번 할 때 마다 초기화
    sum_score = 0   #누적 합 계산

    for j in result:
        if j =='O':
            score += 1  #연속되면 커지기
            sum_score += score  #누적 합 계산
        else:
            score = 0

    print(sum_score)