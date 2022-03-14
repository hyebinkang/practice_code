#10818번
# n = int(input())
# a = list(map(int, input().split()))#입력받은 리스트를 int로 공백구분 할 때
# print(min(a), max(a))

#2562번
# a = []
# for i in range(9):      #예제에서 줄로 나누어진 것들은 for문을 통해 입력 받기
#     n = int(input())
#     a.append(n)
# print(max(a))
# print(a.index(max(a)) + 1)      #a의 최댓값의 index넘버 +1

#2577번
# a = int(input())
# b = int(input())
# c = int(input())
# total = str(a*b*c)      #합산된 결과를 문자열로 바꿔줌
#
# for i in range(10):     #3자리수 3번 곱할 때 최대 자리수는 9자리
#     print(total.count(str(i)))      #count함수를 이용하여 각 문자열 안에서 같은 문자열의 갯수를 세어주는 함수

#3052번
# list_num= []
# list_re= []
# list_unique = []
# for i in range(10):
#     list_num.append(int(input()))
#
#     list_re.append(list_num[i] % 42)
#
# list_unique = set(list_re)#set 함수 = 중복을 제거해 주는 함수
#
# print(len(list_unique)) #len = 함수의 길이, count = 해당 값의 개수를 찾을 때 쓰는 함수
#

# #1546번
# num = int(input())  #과목 수 입력
# score = list(map(int, input().split())) #입력값을 공백을 통해 구분 하고 싶을 때
# edit_score = [] #변환된 점수 넣는 리스트
#
# for i in range(num):
#     edit_score.append(score[i] / max(score) * 100)
#
# print(sum(edit_score)/num)

# #8958번
# num = int(input())  #몇 개를 입력할 것인지
#
# for i in range(num):
#     result = list(str(input())) #문자열 리스트로 받을 때 append사용하기 보다는 지역변수로 만들어줌
#     score = 0   #score 점수 계산, 한번 할 때 마다 초기화
#     sum_score = 0   #누적 합 계산
#
#     for j in result:
#         if j =='O':
#             score += 1  #연속되면 커지기
#             sum_score += score  #누적 합 계산
#         else:
#             score = 0
#
#     print(sum_score)
