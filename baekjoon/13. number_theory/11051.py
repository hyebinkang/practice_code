import math as m

n, k = map(int, input().split())

num = m.factorial(n)//(m.factorial(k)*m.factorial(n-k))

print(num%10007)