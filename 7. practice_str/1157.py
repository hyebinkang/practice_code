new_word = input().upper()

set_word = list(set(new_word))
cnt = []

for i in set_word:
    cnt.append(new_word.count(i))
print(cnt)
print(set_word)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(set_word[cnt.index(max(cnt))])




# 단어의 길이가 1,000,000까지 가능하기때문에
#
# 길이가 최대(n)인 for문 내부에서 count함수를 사용하면
#
# 시간복잡도가 O(n^2)가 되어 시간초과가 날 수도 있습니다.
# import sys
# word = sys.stdin.readline()
# up_word = word.upper()
# alphabet = []
# cnt = []
#
# for i in up_word:
#     alphabet.append(i)
#     cnt.append(alphabet.count(max(i)))
#
# if cnt.count(max(cnt)) > 1:
#     print('?')
# else:
#
#     print(alphabet[cnt.index(max(cnt))])