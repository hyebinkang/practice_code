n, k = map(int, input().split())
cnt = 0

while n != 1:           #n이 1이 될때 까지
    if n%k == 0:        #n이 k로 나누어 떨어지면
        n //=k          #n은 k와 나눈 몫
        cnt +=1         #횟수 추가
    else:               #아니라면
        n -= 1          #n에서 1빼기
        cnt +=1         #횟수 추가

print(cnt)

# #---예시
# n, k = map(int, input().split())
# result = 0
#
# while True:
#     target = (n//k) *k
#     result += n-target
#     n = target
#
#     if n<k:
#         break
#     result +=1
#     n //=k
#
# result += n-1
# print(result)