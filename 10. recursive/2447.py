n = int(input())
star_list = []
def star(x,y):
    while(x!=0):
        if(x%3 == 1 and y%3==1):
            star_list.append('')
        x = x//3
        y = y//3
    star_list.append('*')

for x in range(n):
    for y in range(n):
        star(x,y)

for j in star_list:
    if star_list.index(j) != n//3-1:
        print(j, end='\t')


