

#9498번
# a = int(input())
# if (90<=a<=100):
#     print('A')
# elif(80<=a<=89):
#     print('B')
# elif (70<=a<=79):
#     print('C')
# elif(60<=a<=69):
#     print('D')
# else:
#     print('F')

# #2753번
# year = int(input())
# if ((year%4 == 0) and (year%100 != 0 or year%400 == 0)):
#          print('1')
#
# else: print('0')

#14681번
# x = int(input())
# y= int(input())
# if (x>0 and y>0):
#     print('1')
# elif(x<0 and y>0):
#     print('2')
# elif(x<0and y<0):
#     print('3')
# else:
#     print('4')

#2884번
# h,m = map(int, input().split())
#
# if(m<45):
#     h = h-1
#     m = (m+60)-45
#     if(h<0):
#         h = 23
#     elif(h==0):
#         h = 0
#
# elif(m == 45):
#     m = 0
# else:
#     m = m-45
#
# print(h, m)

#2525번
a, b = map(int, input().split())
c = int(input())

if(b+c < 60):
    b = b+c

else:

    b = b+c
    if(b+c>=60):
        a = a+1
        b = b-60
        if(b>=60):
            a = a+1
            b = b-60
    if(a >= 24):
        a = a-24
    print(a,b)
