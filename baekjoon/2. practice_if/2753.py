year = int(input())
if ((year%4 == 0) and (year%100 != 0 or year%400 == 0)):    #4로 나누고 (100으로 나누었을 때 0이 아니거나 400으로 나누었을 때)중 하나 이면 윤년
         print('1')

else: print('0')
#윤년 확인하기