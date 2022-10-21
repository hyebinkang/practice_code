import math
import sys
#
# num_list = []
# count = 0
#
# n, m = map(int, sys.stdin.readline().split())
#
# num = math.factorial(n)//(math.factorial(m)*math.factorial(n-m))
#
# while num !=0:
#     a = num % 10
#     if a !=0:
#         print(count)
#         break
#     else:
#         count +=1
#         num_list.append(num % 10)
#         new_num = num//10
#         num = new_num

n, m = map(int, sys.stdin.readline().split())

def two(n):                 #10은 2와 5의 곱으로 이루어짐
    n2 = 0                  #즉, n,m이 가지고 있는 2와 5의 개수, m-n이 가지고 있는 2와 5의 개수를 따진다
    while(n!=0):
        n//=2
        n2 += n
    return n2
def five(n):
    n5 = 0
    while(n!=0):
        n//=5
        n5 += n
    return n5

print(min(two(n)-two(m)-two(n-m), five(n)-five(m)-five(n-m)))