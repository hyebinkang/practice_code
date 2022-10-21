total_price = int(input())      #결제된 가격
total_num = int(input())        #구매한 물건의 개수
total = 0                       #총 가격
for i in range(total_num):
    price, num = map(int, input().split())      #가격과 개수 입력받기

    total += price*num          #가격*개수를 총 가격에 더하며 계산

if total == total_price:        #처음 입력받은 값과 계산한 값이 같으면 Yes 아니라면 No출력
    print('Yes')
else:
    print('No')