n = int(input())
result = 0
for i in range(1, n+1):             #1부터 n 까지
    m = list(map(int, str(i)))      #map함수를 사용하여, str 하나씩 나누어 int로 저장
    result = i+sum(m)               #i+ 리스트의 합(= 입력받은 숫자 n을 각 자리수로 나눈것)

    if(result == n):                #result 와 n이 같다면
        print(i)                    #i출력 = 분해합
        break
else:                               #숫자n 까지에도 만족하는 수가 없다면 0출력
    print(0)