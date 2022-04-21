import sys
n = int(sys.stdin.readline())
num = [0] * 10001                       #10000까지의 수를 모두 0으로 설정

for _ in range(n):
    temp = (int(sys.stdin.readline()))  #입력받은 수를 num의 인덱스 값으로 설정하여 +1씩 증가
    num[temp] += 1


for i in range(10001):
    if num[i] !=0:                      #만약 i가 0이 아니면
        for j in range(num[i]):         #num[i] 만큼 해당하는 i의 값을 출력
            print(i)
