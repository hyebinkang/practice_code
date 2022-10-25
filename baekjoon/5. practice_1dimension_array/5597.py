stu = [i for i in range(1,31)]      #1부터 30까지 먼저 리스트에 저장

for j in range(28):
    num = int(input())
    stu.remove(num)                 #들어오는 수 하나씩 제거

for no in stu:
    print(no)                       #나머지 출력