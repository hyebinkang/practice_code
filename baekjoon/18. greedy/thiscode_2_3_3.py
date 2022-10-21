n, m = map(int, input().split())
result = []                                 #result리스트로 했을 때

for i in range(n):
    line = list(map(int, input().split()))

    result.append(min(line))                #최솟값을 result에 저장

print(max(result))                          #최솟값 중 가장 큰 값 출력

# #예시-----
# n, m = map(int, input().split())
#
# result = 0                                #result 를 0으로 했을 때
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)           #result값과, min_value값 비교하여 큰 수를 result로
#
# print(result)