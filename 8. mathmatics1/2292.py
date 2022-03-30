n = int(input())    #숫자 입력
room = 1    #1부터 시작
six_room = 6    #6의 배수로 증가하는 규칙
count = 1   #바퀴, 최소 경로 구하기
while n > room: #n이 room 보다 클 때 까지
    count += 1  #최소 경로 +1
    room += six_room    #6의 배수로 증가, 한 바퀴 안에 있는 마지막 수
    six_room += 6   #6을 더해줌
print(count)
