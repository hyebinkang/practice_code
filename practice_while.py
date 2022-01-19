# #10952번
# a,b = map(int, input().split())
# while a+b != 0:
#     print(a+b)
#     a,b = map(int, input().split())
#     if a+b == 0:
#         break

# #10951번
# while True:#while 1과 같은 의미
#     try:
#         a,b = map(int, input().split())
#         print(a+b)
#     except:
#         break

#try문에 실행코드를, except문에 예외처리 코드를 작성

# #1110번
#
# init_number = int(input())  #초기 숫자 입력
# num = init_number   #초기숫자를 계산할 숫자로 변경
# cycle = 0   #몇 회 돌았는지 cycle 횟수
# new_num = 0 #계산하여 만들어진 새로운 숫자
#
# while True:
#     a = num // 10   # num의 십의 자리
#     b = num % 10    #num의 일의 자리
#     new_num = b*10 + (a+b) % 10 #계산하여 만든 새로운 new_num
#     cycle += 1  #횟수 추가
#     num = new_num   #새로운 숫자를 다시 계산에 사용해야하니 계산 되는 숫자로 만들어야함
#     if init_number == new_num:  #초기 숫자와 새로운 숫자가 같으면 종료
#         break
# print(cycle)
# 한 줄씩 천천히 생각해야함