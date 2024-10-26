n = str(input())        #문자 받기
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#알파벳 미리 리스트로 만들어두기
for i in n:                 #for문으로 n을 돌았을 때
    if i in alphabet:
        print(alphabet.index(i)+1, end=' ')     #i번째 문자가 알파벳 리스트에 있으면, 문자의 인덱스 값+1을 출력하기