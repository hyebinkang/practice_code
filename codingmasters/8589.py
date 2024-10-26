# n = int(input())
# distance = []
# people=[]
# cnt = [0 for i in range(n)]
# people_cnt = [0 for i in range(n)]
# for i in range(n):
#     apt, num = map(int, input().split())
#     distance.append(apt)
#     people.append(num)
#
# for j in range(n):
#     for k in range(n):
#         cnt[j] += abs(distance[j]-distance[k])
#         people_cnt[j] += abs(people[j]-people[k])
#
# print(cnt)
# print(min(cnt))
# print(people_cnt)
# print(min(people_cnt))

# def find_optimal_waste_station(N, apartments):
#     total_distance = float('inf')
#     optimal_station = 0
#
#     for station in range(1, N + 1):
#         distance = 0
#         for apt in apartments:
#             distance += abs(apt - station)
#
#         if distance < total_distance:
#             total_distance = distance
#             optimal_station = station
#
#     return optimal_station
#
#
# # 입력 받기
# N = int(input())
# apartments = list(map(int, input().split()))
#
# # 최적의 분리수거장 찾기
# optimal_station = find_optimal_waste_station(N, apartments)
# print(optimal_station)
#
n = int(input())
trash = []
person=[]
for i in range(n):
    apt, people = map(int, input().split())
    trash.append(apt)
    person.append(people)

diff = []
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt +=abs(trash[i]-trash[j])
    diff.append(cnt*person[i])


print(diff.index(min(diff)) +1)

# n = int(input())
# trash =[]
# person=[]
# for i in range(n):
#     apt, people = map(int, input().split())
#     trash.append(apt)
#     person.append(people)
#
# trash.sort()
