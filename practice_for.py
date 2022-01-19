# #10950번
# t= int(input())
#
# for i in range(t):
#     a,b = map(int, input().split())
#     print(a+b)

#8393번
# n = int(input())
# sum = 0
#
# for i in range(n+1):
#     sum += i
#     print(sum)

#15552번
# import sys
#
# t= int(input())
#
# for i in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

#2741번
# N = int(input())
# for i in range(N+1):
#     if i == 0:
#         pass
#     else:
#         print(i)

# #2742번
# N = int(input())
# for i in range(N+1):
#     result = N-i
#     if result == 0:
#         pass
#     else:
#         print(result)


# #11021번
# t = int(input())
# for i in range(t):
#     a,b = map(int, input().split())
#     print("Case #%s: %s"%(i+1, a+b))

# #11022
# t = int(input())
# for i in range(t):
#     a,b = map(int, input().split())
#     print("Case #%s: %s + %s = %s" %(i+1, a, b, a+b))

#2438번
# n = int(input())
# for i in range(n):
#     print("*" * (i+1))
#
# #2439번
# n = int(input())
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * i)

# #10871번
# n,x = map(int, input().split())#공백으로 숫자 구분 삽입
# a = list(map(int, input().split()))
# for i in range(n):
#     if a[i] < x:
#         print(a[i], end=" ")

