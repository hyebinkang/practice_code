# m, n = map(int, input().split())
#
# for i in range(m, n):
#     cnt = 0
#     for j in range(2, i+1):
#         if(i % j == 0):
#             cnt +=1
#     if(cnt == 1):
#         print(i)


m,n = map(int, input().split())
array = []

for i in range(m, n+1):
    prime = True    #bool타입 선언
    if i ==1:
        continue    #continue와 pass 차이,
    for j in range(2, int(i**0.5) +1):  #왜 0.5인지
        if i % j ==0:
            prime = False
            break
    if prime == True:   #if prime: 도 같은 의미
        array.append(i)
        print(i)





