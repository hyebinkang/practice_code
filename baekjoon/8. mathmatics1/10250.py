t = int(input())
x = 0   #층
y = 0   #방 번호
for i in range(t):
    h,w,n = map(int, input().split()) #h: 호텔 층 수, w:각 층의 방, n:몇 번째 손님

    x = n % h   #층 = 손님 / 층 수의 나머지
    y = n // h + 1  #몫에 +1
    if(x == 0): #나머지가 0일 때
        x = h   #층 = h
        y -=1   # 몫에서 -1

    if(x >= 10 and y >=10): #x,y가 두 자리 수 한 자리 수 일 때 호수 구분하여 출력
        print(x,y, sep='')

    elif(x>=10 and y < 10):
        print(x,0,y, sep='')

    elif(x<10 and y >=10):
        print(x,y, sep='')

    else:
        print(x,0,y, sep='')
