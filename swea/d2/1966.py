t = int(input())        #횟수

for i in range(t):

    n = int(input())        #입력하는 개수
    n_list = sorted(list(map(int, input().split())))[:n]    #입력받은 리스트 정렬
    print("#{0}".format(i+1), end=' ')
    for j in n_list:
        print(j, sep=' ', end=' ')
    print()         #줄 바꿈


