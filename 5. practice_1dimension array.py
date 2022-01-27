#10818번
# n = int(input())
# a = list(map(int, input().split()))#입력받은 리스트를 int로 공백구분 할 때
# print(min(a), max(a))

#2562번
# a = []
# for i in range(9):      #예제에서 줄로 나누어진 것들은 for문을 통해 입력 받기
#     n = int(input())
#     a.append(n)
# print(max(a))
# print(a.index(max(a)) + 1)      #a의 최댓값의 index넘버 +1

#2577번
# a = int(input())
# b = int(input())
# c = int(input())
# total = str(a*b*c)      #합산된 결과를 문자열로 바꿔줌
#
# for i in range(10):     #3자리수 3번 곱할 때 최대 자리수는 9자리
#     print(total.count(str(i)))      #count함수를 이용하여 각 문자열 안에서 같은 문자열의 갯수를 세어주는 함수