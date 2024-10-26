t= int(input())

for _ in range(t):
    grass = input()
    count = 0
    for i in range(len(grass)):
        if grass[i] == '(' and grass[i+1] == ')':
            count +=1
        elif grass[i]=='|' and grass[i+1] == '|':
            count +=1
        elif grass[i] == '|' and grass[i+1] == ')':
            count +=1
    print("#{0}".format(_+1), count)