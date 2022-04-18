N = int(input())

student = []                        #키, 몸무게 담을 리스트 이중리스트 형태로

for i in range(N):
    student.append(list(map(int, input().split())))     # 두개의 값 입력 받기


for weight, height in student:      #student 값을 각각 weight, height로
    rank = 1                        #초기값 설정
    for j, k in student:
        if weight < j and height < k:   #밖의 for문 weight랑, j 비교, height랑 k비교
            rank +=1                    #j와 k가 다 크다면, 가장 최대인 rank
    print(rank, end=' ')