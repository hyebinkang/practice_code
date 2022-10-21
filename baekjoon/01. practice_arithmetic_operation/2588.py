first_number = int(input())

second_number = int(input())
a=second_number // 100
b= (second_number%100)//10
c = second_number%100%10

d = first_number * c
e = first_number * b*10
f = first_number * a*100

g = d+e+f

print(d)
print(e//10)
print(f//100)
print(g)
