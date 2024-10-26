t = int(input())

for i in range(t):
    case = int(input())
    score = [0 for _ in range(101)]                     #초기의 100개 점수를 모두 0으로 만들어줌
    student = list(map(int, input().split()))           #학생 점수 입력

    for j in student:                                   #학생 점수 별 인덱스에 +1씩 더함
        score[j] +=1

    best_num = max(score)                               #최고 점수 저장
    best= []                                            #최고 점수가 여러개일 때 인덱스 값 저장
    for k in range(101):
        if score[k] == best_num:                        #score값이 최고 점수와 같다면
            best.append(score.index(score[k]))          #best에 저장 후 값을 0으로 만들어준다
            score[k] = 0


    print("#{0} {1}".format(case, max(best)))           #여러 최빈수 안에서 가장 큰 값 출력