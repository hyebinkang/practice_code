import sys
n = int(sys.stdin.readline())
word = []
for _ in range(n):
    word.append(sys.stdin.readline().strip())       #sys로 받는 입력은 '\n'을포함하기 때문에 strip()을 써준다.

set_word = list(set(word))                  #set이용해서 중복제거
set_word.sort()                             #알파벳으로 먼저 정렬 한 후
set_word.sort(key = len)                    #길이에 맞춰 정렬을 한다

for i in set_word:
    print(i)