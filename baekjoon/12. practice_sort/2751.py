import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))        #숫자 입력

for _ in sorted(num):                            #정렬된 리스트 출력
    sys.stdout.write(str(_) + '\n')