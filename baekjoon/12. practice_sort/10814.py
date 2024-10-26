from operator import itemgetter     #다중 수준 정렬, sorted key에 적용되는 방법
import sys
n = int(sys.stdin.readline())
people = []

for _ in range(n):
    age, name = map(str, sys.stdin.readline().split())      #문자로 두 변수의 입력값을 받고
    people.append((int(age), str(name)))                    #age는 int로 , 이름은 str로 받는다.

# people.sort(key = itemgetter(0))          #itemgetter이용, 0번째에 위치하는 age를 기준으로 정렬
people.sort(key = lambda age: (age[0]))     #람다 함수를 사용하여, age기준으로 정렬

for i in range(n):
    print(people[i][0], people[i][1])       #같은 i가 존재할 경우 순서대로 출력
