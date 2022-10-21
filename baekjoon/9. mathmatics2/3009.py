x_list= []                 #입력된 x받는 list
y_list = []                 #입력된 y 받는 list
for i in range(3):
    x, y = map(int, input().split())        #x,y값 입력
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j]) == 1:        #리스트 안의 j번째 숫자를 count
        x1 = x_list[j]                      #count가 1 이면 할당
    if y_list.count(y_list[j]) == 1:
        y1 = y_list[j]
print(x1,y1)