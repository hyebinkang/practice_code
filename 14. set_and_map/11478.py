s = input()

arr=[]

for i in range(len(s)):             #s의 길이만큼 반복
    for j in range(len(s)+1):
        arr.append(s[j:j+i])        #처음부터 1씩 늘어갈 때 마다 append

print(len(set(arr)))                #arr을 중복제거한 길이를 출력
