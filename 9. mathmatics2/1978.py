n = int(input())    #숫자 개수 입력
num_list = list(map(int, input().split()[:n]))  #숫자 리스트 입력
prime = 0   #소수의 개수

if 1 in num_list:   #1은 소수가 아님
    num_list.remove(1)

for i in num_list:  #리스트 안 순서대로 for문
    cnt = 0 #현재 0으로 나누어 떨어진 개수, 소수: 1과 자기자신을 약수로 하는 수 (즉, 소수 = 나머지가 자기자신 뿐)
    for j in range(2, i+1): #1은 소수에 포함되지 않음, i+1만큼 for문
        if i % j == 0:
            cnt +=1
    if(cnt == 1):   #cnt가 1이면(=소수)
        prime += 1  #소수에 개수 추가

print(prime)