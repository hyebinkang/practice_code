fixed, varied, now = map(int, input().split())  #고정비용, 가변비용, 현재 값

if varied >= now :  #가변비용이 현재 비용보다 크다면
    print(-1)
else:   #현재비용 - 가변비용을 고정비용으로 나눈 후 +1
    print((fixed // (now-varied)) + 1)
# fixed, varied, now = map(int, input().split())
#
# for i in range(fixed):
#     cost = now * i
#     produce = fixed + varied * i
#     if(cost > produce):
#         print(produce)
#         print(i)
#         break
#     if (varied >= now):
#         print(-1)
