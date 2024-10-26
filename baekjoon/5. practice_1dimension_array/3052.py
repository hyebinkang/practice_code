list_num= []
list_re= []
list_unique = []
for i in range(10):
    list_num.append(int(input()))

    list_re.append(list_num[i] % 42)

list_unique = set(list_re)#set 함수 = 중복을 제거해 주는 함수

print(len(list_unique)) #len = 함수의 길이, count = 해당 값의 개수를 찾을 때 쓰는 함수

