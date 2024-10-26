t = int(input())

for i in range(t):
    p,q,r,s,w = map(int, input().split())       #p:1L당 요금, q: r리터 이하 요금, r:기준 리터, s:초과시 1L당 요금, w: 사용량

    a= p*w          #a사 요금 계산
    if w>r:         #b사 요금 계산
        b=q+(w-r)*s
    else:
        b=q

    if a>b:         #비교
        print("#{0}".format(i+1), b)
    else:
        print("#{0}".format(i+1), a)
