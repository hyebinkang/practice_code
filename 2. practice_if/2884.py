h,m = map(int, input().split())

if(m<45):
    h = h-1
    m = (m+60)-45
    if(h<0):
        h = 23
    elif(h==0):
        h = 0

elif(m == 45):
    m = 0
else:
    m = m-45

print(h, m)

#오븐 계산, 시간 계산 하기