t = int(input())

for i in range(t):
    s = input()
    spell = ['b','d','p','q']                   #bdpq로 이루어진 문자열
    change = ['d', 'b','q', 'p']                #거울에 비친 모습
    word= []
    for j in s:
        word.append(change[spell.index(j)])     #인덱스 번호가 같은 곳의 문자를 append

    print("#{0}".format(i+1), end=' ')
    for k in word[::-1]:                        #거꾸로 출력
        print(k, end='')
    print()