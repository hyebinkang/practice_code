# n, m = map(int, input().split())
# s = []                            #리스트
# count = 0
#
# for _ in range(n):
#     s.append(input())             #s의 단어들을 저장
#
# for i in range(m):
#     a = str(input())              #s와 비교할 문자열 a를 입력하여 비교
#     if a in s:
#         count +=1
# print(count)

n, m = map(int, input().split())
s = {}                                  #딕셔너리
count = 0

for _ in range(n):
    put = input()
    s[put] = True                       #key를 put에 입력받은 단어로, value를 True로

for i in range(m):
    a = input()
    if a in s.keys():                   #s의 key와 a를 비교
        count +=1
print(count)