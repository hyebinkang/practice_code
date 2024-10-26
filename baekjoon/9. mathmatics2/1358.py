w, h, x, y, p = map(int, input().split())       #직사각형 (w,h), 원(x,y), 선수(p)
count = 0

for _ in range(p):                              #선수 횟수만큼 for문
    new_x, new_y = map(int, input().split())

    if x <= new_x <= x+w and y <= new_y <=y+h:          #직사각형 안에 들어오는 범위
        count +=1
    elif (new_x - x)**2 + (new_y-(y+h//2))**2 <= (h//2)**2:     #(x, y+r)이 중심인 반원에 들어오는 범위
        count +=1
    elif (new_x-(x+w))**2 + (new_y-(y+h//2))**2 <= (h//2)**2:   #(x+w, y+r)이 중심인 반원에 들어오는 범위
        count +=1
    else:
        continue        #모두 속하지 않는 경우

print(count)