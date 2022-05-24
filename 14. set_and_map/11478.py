s = input()

arr=[]

for i in range(len(s)):
    for j in range(len(s)+1):
        arr.append(s[j:j+i])

print(len(set(arr)))
