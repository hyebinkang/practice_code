a = int(input())    #약수의 개수 입력(1과 자기자신 제외한 개수)

arr = list(map(int, input().split()))       #약수입력
print(min(arr)*max(arr))        #1과 자기자신을 제외 했기 때문에 주어진 수에서 최솟값과 최댓값을 더하면 약수n이 됨


#--틀린거--
# n = []
# num = []
# for i in range(1, 1000001):       # 1과 50사이 수
#     for j in arr:
#         if(i%j == 0):     #arr로 받은 수를 1~50까지의 수로 나눈다
#             n.append(i)   #나머지가 0이면 n에 저장
#
# for k in range(len(n)):       #n의 개수만큼 실행
#     if(n.count(k) == a):      #n안에서 k번째의 count가 a와 같으면
#         if(k not in arr):     #그리고 arr에 없으면
#             num.append(k)     #num에 append
#
# print(min(num))           #최솟값을 출력