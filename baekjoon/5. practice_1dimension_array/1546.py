num = int(input())  #과목 수 입력
score = list(map(int, input().split())) #입력값을 공백을 통해 구분 하고 싶을 때
edit_score = [] #변환된 점수 넣는 리스트

for i in range(num):
    edit_score.append(score[i] / max(score) * 100)

print(sum(edit_score)/num)