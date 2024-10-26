t= int(input())

for i in range(t):
    num = list(map(int, input().split()))

    num.remove(max(num))        #최소, 최대 수 제거
    num.remove(min(num))

    print("#{0}".format(i+1), round(sum(num)/len(num)))     #평균값 반올림 후 결과 출력