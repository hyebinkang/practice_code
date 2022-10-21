s = input()

result = int(s[0])                      #문자열의 첫번째를 result 로 설정
for i in range(1, len(s)):              #위에서 첫번째를 result로 했으니까 0을 제외시켜줌
    num = int(s[i])                     #i를 int로
    if num <=1 or result <=1:           #둘 중 하나라도 0,1인 경우 +를 했을 때가 더 유리하기에 더하기
        result +=num
    else:                               #2이상이면 *를 한다
        result *= num

print(result)
