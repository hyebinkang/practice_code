number = input()    #숫자 입력, 문자열로 받기
re_num = []         #숫자를 역순으로 하는 문자열 넣기

for i in number:    #숫자를 각각 한 원소로 저장
    re_num.append(i)

re_num.reverse()    #순서대로 받은 원소를 역순으로 나타내기
num = ''.join(re_num).split()   #공백을 기준으로 숫자 구분해서 원소 만들기

if (num[0] > num[1]):   #리스트 안의 0번째 원소가 1번째 보다 크면
    print(num[0])       #0출력
else:
    print(num[1])       #1출력
