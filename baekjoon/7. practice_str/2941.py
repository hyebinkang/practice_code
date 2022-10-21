word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] #크로아티아 알파벳 리스트

for i in croatia:   #croatia단어들 for문
    word = word.replace(i, '*') #단어 안에 croatia 알파벳이 있다면 +모양으로 바꿈

print(len(word))    #*모양으로 바꾼 후의 word의 길이 = croatia알파벳 + 영어 알파벳의 개수
