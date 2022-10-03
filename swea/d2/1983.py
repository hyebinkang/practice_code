t= int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0','B-', 'C+', 'C0', 'C-', 'D0']

def cal(i):
    new_score = []                                  # 문자로 변환한 값 넣는 리스트
    student_score = total_score[student - 1]        #원하는 학생의 점수

    for k in range(people):

        while total_score != []:
            best_score = max(total_score)           # 최고점수

            if new_score.count(score[k]) < people//10:              #동일 평점 인원만큼
                if best_score == student_score:
                    best_score = score[k]
                    return print("#{0}".format(i+1), best_score)        #return으로 함수 종료

                else:
                    total_score.remove(best_score)
                    best_score = score[k]
                    new_score.append(best_score)
            else:                                                   #동일 평점 인원이 같거나 많다면 break -> for (변수 증가)
                break


for i in range(t):

    people, student = map(int, input().split())             #학생수, 원하는 학생 번호
    total_score = []                                        #학생 전체의 총점

    for j in range(people):
        mid, fin, asi = map(int, input().split())
        total_score.append(mid*0.35 + fin*0.45+ asi*0.2)

    cal(i)
