def self_number():
    number_list = list(range(1,10000))  #1 ~ 10000까지 숫자를 리스트에 저장

    for i in range(10000):
        mil_n = i // 10000              #범위 내에서 최고 숫자가 10000이고, 최대 5자리이기 때문에 만 자리에 해당하는 수는 10000밖에 없음
        tho_n = i // 1000               #천의 자리
        hun_n = i % 1000 // 100         #백의 자리
        ten_n = i % 1000 % 100 // 10    #십의 자리
        one_n = i % 1000 % 100 % 10     #일의 자리
        next_n = i + mil_n+ tho_n+ hun_n +ten_n +one_n  #'해당하는 수'(=리스트 i번째)와 '각 자리수' 를 더해서 생성자 계산

        if(next_n in number_list):      #만약 생성자로 만든 수가 리스트 안에 있으면 그 수를 제거한다
            number_list.remove(next_n)

    for j in range(len(number_list)):   #결과 출력
        print(number_list[j])

    return number_list

self_number()                           #함수로 만들었을 땐 결과를 부르도록 꼭 써줘야 함

# 셀프넘버: n + n의 자리수에 있는 숫자들을 다 더해서 다음 숫자를 만듬(=생성자)
#       이 때, 생성자에 해당 하지 않는 수가 셀프 넘버에 해당됨