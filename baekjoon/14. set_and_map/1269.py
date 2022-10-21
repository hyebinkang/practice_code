import sys
a, b = map(int, sys.stdin.readline().split())
#
# a_list = list(map(int, sys.stdin.readline().split()))[:a]
# b_list = list(map(int, sys.stdin.readline().split()))[:b]
# ori_a = a_list.copy()
# ori_b = b_list.copy()
#
# for i in range(b):                #for 문으로 각 리스트 안에 있는 공통 요소들을 찾아낸다
#     if b_list[i] in a_list:
#         a_list.remove(b_list[i])
#
# for j in range(a):
#     if ori_a[j] in b_list:
#         b_list.remove(ori_a[j])
#
# print(len(a_list)+len(b_list))

a_set = set(map(int, input().split()))  #set으로
b_set = set(map(int, input().split()))

print(len(a_set^b_set))     #^ 대칭차집합 구하는 연산자