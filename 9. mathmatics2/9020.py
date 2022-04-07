import sys
def isPrime(num):
    if num == 1:            #1은 소수가 아님
        return False
    else:
        for i in range(2, int(num**0.5)+1): #2부터 num의 제곱근 +1의 범위까지
            if num%i == 0:
                return False        #소수가 아닌 것들
        return True           #소수인 것들에 True반환

t = int(sys.stdin.readline())
all_num = [x for x in range(2, 10001)]  #범위 안 숫자들 저장
prime = []  #소수인 숫자들만 뽑기

for a in all_num:
    if isPrime(a):
        prime.append(a)

for i in range(t):
    n = int(sys.stdin.readline())
    if n <= 3:
        continue
    list_gold = []      #n-k값 저장
    list_k = []         #k값 저장
    list_diff=[]        #gold-k값 저장 -> 차이가 최소화인 값의 인덱스값 나타내기 위해서

    for k in prime:     #prime인 숫자들에 대한 for문
        gold = n - k    #gold값 계산
        if (isPrime(gold)):     #gold가 소수이면
            if gold-k >= 0:     #그 차이가 0보다 크다면
                list_gold.append(gold)      # 각 값을 각 리스트에 저장
                list_k.append(k)
                list_diff.append(gold-k)
            else:
                break
        else:
            if gold-k>=0:   #gold-k가 0,양수이면 continue
                continue
            else:           #아닌 경우 종료
                break

    j = list_diff.index(min(list_diff))     #gold-k의 차이가 가장 작은 값의 인덱스 값을 변수로 저장
    if (list_gold[j] >= list_k[j]):         #그 변수의 인덱스에 해당하는 값들을 비교
        print(list_k[j],list_gold[j], sep=' ')
    else:
        print(list_gold[j],list_k[j],sep=' ')
