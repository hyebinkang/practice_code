tc = int(input())
ten = 0
for _ in range(tc):
    n = int(input())
    n = round(n, 2)
    print(n)

    while n > 10:

        rest = n%10
        ten += 1

        num = n//10
        n = num

    result = n/10
    ten +=1




    print("#",_+1," ",result,"*",10,"^",ten, sep="")