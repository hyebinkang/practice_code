x = int(input())    #몇 회 반복 할지 입력 받기

for i in range(x):
    a, b = map(str, input().split())    #공백으로 두 문자를 받고
    a = int(a)                          #a를 int로 변환
    for j in b:                         #문자열 b에 대해 반복
        print(a*j, end='')              #b의 각 자리 글자 * 횟수, end=''를 사용하여 줄 바꿈 없이 한 줄로 이어 나오게 함
    print()                             #다시 첫 줄로 돌아가야 하기 때문에 넘겨줘야 답으로 인정
