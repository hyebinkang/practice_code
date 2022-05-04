a, b = 1, 0                 #a,b 초기화 먼저
while(a!=b):                #a와 b가 같은 경우가 0,0 인 경우 밖에 없음
    a, b = map(int, input().split())    #a,b입력
    if (a==b):              #a,b입력 후 같으면 break
        break
    elif(b%a == 0 and b>a):   #b가 더 클 때 a로 나누어 나머지가 0이면 약수
        print('factor')
    elif(a%b == 0 and b<a): #a가 더 클 때 b로 나누어 나머지가 0이면 배수
        print('multiple')
    else:
        print('neither')    #두 경우 모두 아닐 땐 neither
