#-----라이브러리 없이 풀기-----
t= int(input())     #test횟수 입력

encode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
          ] #encode문자표

for i in range(t):
    text = input()              #문장입력
    string = ''                 #이진수로 바뀌는 문장 저장
    decode = ''
    start = 0                   #8비트씩 나누기[0:8] -> 8비트
    fin = 8
    for j in text:
        j = encode.index(j)             #text의 한 문자를 decode에 해당하는 인덱스 번호로 바꾸기
        string += '{0:06b}'.format(j)   #그 문자를 6비트의 이진수로 표현

    for k in range(len(string)//8):     #이진수를 8비트씩 나눌 것이므로 범위도 8비트로 나누어줌
        result = string[start:fin]      #이진수를 8비트씩 자른 것
        sen = int(str(result), 2)       #십진수로 변환
        decode += chr(sen)              #아스키코드로 변환한 문자 이어 붙이기
        start +=8                       #다음 8비트를 자르기
        fin +=8

    print("#{0}".format(i+1), decode)


# #---라이브러리로 풀기---
import base64                                       #라이브러리 설치
t = int(input())

for i in range(t):
    text_base64_str = input()                       #이미 인코딩 되어있는 문자
    text_bytes = base64.b64decode(text_base64_str)  #입력된 문자를 bytes타입으로 디코딩
    text = text_bytes.decode('ascii')               #아스키 코드로 디코딩

    print(text)
