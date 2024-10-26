n = int(input())

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j]!=word[j+1]:          #연속된 두 문자가 다를 때
            if word[j] in word[j+1:]:   #j번째 문자가 j+1부터 끝까지의 문자 안에 있을 때
                n-=1                    #단어의 수에서 -1
                break
print(n)