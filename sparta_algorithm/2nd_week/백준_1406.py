word = list(input())
n = int(input())
cursor = len(word)
for _ in range(n):
    put = list(map(str, input().split()))

    if put[0] == 'L':
        if cursor == 0:
            continue
        cursor -=1
    elif put[0] == 'R':
        if cursor == len(word):
            continue
        cursor +=1
    elif put[0] == 'B':
        if cursor != 0:
            word.remove(word[cursor-1])
    elif put[0] == 'P':
        word.insert(cursor, put[1])
print(word)



