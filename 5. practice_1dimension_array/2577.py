a = int(input())
b = int(input())
c = int(input())
total = str(a*b*c)      #합산된 결과를 문자열로 바꿔줌

for i in range(10):     #3자리수 3번 곱할 때 최대 자리수는 9자리
    print(total.count(str(i)))      #count함수를 이용하여 각 문자열 안에서 같은 문자열의 갯수를 세어주는 함수
