t= int(input())

for i in range(t):
    text = str(input())

    for j in range(len(text)):
        start = text[0]                 #첫 시작 문자 저장

        if text[j+1] == start:          #start 이후 부터 비교
            if text[j+2] == text[1]:            #만약 글자가 같을 때 다음 글자도 같다면(단, aaacaaac와 같은 반례가 존재하는 코드임)
                word = text[0:j+1]              #단어 슬라이스
                print("#{0}".format(i+1), j+1)
                break
