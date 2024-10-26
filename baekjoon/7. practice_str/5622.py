word = input()  #단어 입력
english = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO','PQRS','TUV', 'WXYZ']  #다이얼 안의 영어 끼리 한 단어로 취급
result= 0   #숫자의 합

for i in word:  #단어 한 글자씩 분리
    for j in english:   #영어 한 글자씩 분리
        if i in j:  #단어의 글자가 영어의 글자 안에 있을 때
            result += english.index(j) + 3  #영어 인덱스에서 +3 더하기

print(result)