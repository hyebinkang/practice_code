import math
import sys

num_list = []
count = 0

n, m = map(int, sys.stdin.readline().split())

num = math.factorial(n)//(math.factorial(m)*math.factorial(n-m))

while num !=0:
    a = num % 10
    if a !=0:
        print(count)
        break
    else:
        count +=1
        num_list.append(num % 10)
        new_num = num//10
        num = new_num

# for i in num_list:
#     if i == 0:
#         count +=1
#     else:
#         print(count)
#         break
