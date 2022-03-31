a = []
for i in range(9):      #예제에서 줄로 나누어진 것들은 for문을 통해 입력 받기
    n = int(input())
    a.append(n)
print(max(a))
print(a.index(max(a)) + 1)      #a의 최댓값의 index넘버 +1