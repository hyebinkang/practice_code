import math
a, b, v = map(int, input().split()) #a,b,v입력

day = (v-a)/(a-b) +1    #공식 v = (a-b) * day + a 식에서 day를 기준으로 정리,야
print(math.ceil(day))   # 하루 지난 시점 +1 까지 더해 주어야 함

# -------시간초과----------
# day = 0
# m = 0
# while day < v:
#
#     m += a
#     day +=1
#     if (m >= v):
#         break
#     m -= b
