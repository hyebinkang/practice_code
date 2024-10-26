t = int(input())

for i in range(t):
    ymd = str(input())      #문자로 입력

    yyyy = ymd[0:4]         #인덱스 번호 0~3까지 yyyy로
    mm = ymd[4:6]           #4~6은 mm
    dd = ymd[6:]            #6부터 마지막은 dd


    if 1 <= int(mm) <= 12:      #mm이 해당하면 각 월에 맞춰서 일자 찾고 결과 출력
        if int(mm) == 1 and 1<= int(dd)<=31:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 2 and 1<= int(dd)<=28:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 3 and 1<= int(dd)<=31:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 4 and 1<= int(dd)<=30:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 5 and 1<= int(dd)<=31:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 6 and 1<= int(dd)<=30:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 7 and 1<= int(dd)<=31:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 8 and 1<= int(dd)<=31:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 9 and 1<= int(dd)<=30:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 10 and 1<= int(dd)<=31:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 11 and 1<= int(dd)<=30:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        elif int(mm) == 12 and 1<= int(dd)<=31:
            print('#',i+1,' ', yyyy,'/',mm,'/',dd, sep ='')

        else:                                   #dd가 맞지 않을 때 출력
            print('#',i+1,' ', -1, sep='')

    else:                                       #mm이 맞지 않을 때 출력
        print('#',i+1,' ', -1, sep='')
