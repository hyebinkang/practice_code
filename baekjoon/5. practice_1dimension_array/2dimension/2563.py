n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]     #100*100 도화지

for i in range(n):
    a,b = map(int, input().split())                     #두 수 입력
    for j in range(a, a+10):                            #각 색종이의 길이가 10
        for k in range(b, b+10):
            arr[j][k] = 1                               #1로 영역 표시
count = 0
for row in arr:
    count+= row.count(1)                                #각 행 마다 1의 개수를 더하기
print(count)
