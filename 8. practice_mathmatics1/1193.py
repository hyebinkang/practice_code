n = int(input())

x = 1   #분자
y = 1   #분모

cross = 1
avg_cross = 0


while n > avg_cross:

    avg_cross += 1

    for count in range(1, cross+1):
        if(cross % 2 == 0):
            if(count % 2 ==0):
                x = avg_cross-cross +1
                y = cross
                break
            else:
                x = cross
                y = abs(avg_cross-cross)
                break

        else:
            if (count % 2 == 0):
                x = avg_cross - cross +1
                y = cross
                break
            else:
                x = cross
                y = abs(avg_cross - cross) +1
                break
    count += 1
    if(count == cross):
        cross +=1
        count = 1




print(x,'/',y, sep='')