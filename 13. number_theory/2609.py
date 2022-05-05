a,b = map(int, input().split())
arr= []

for i in range(1, min(a,b)+1):      #1부터 ~ a,b중 최소값+1 만큼 의 수를 반복
    if(a%i == 0 and b%i==0):        #a와 b가 둘다 나누어 떨어져야 함
        arr.append(i)               #해당하는 수 저장

print(max(arr))                     #리스트 안의 최댓값 = 최대공약수
print(max(arr)*a//max(arr)*b//max(arr)) #최대공약수로 각 a,b를 나눈 것의 몫을 곱하면 최소공배수가 된다.