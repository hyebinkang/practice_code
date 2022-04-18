N = int(input())

student = []

for i in range(N):
    student.append(list(map(int, input().split())))


for weight, height in student:
    rank = 1
    for j, k in student:
        if weight < j and height < k:
            rank +=1
    print(rank, end=' ')