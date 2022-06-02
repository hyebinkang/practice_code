import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))      #가지고 있는 카드
arr.sort()

M = int(sys.stdin.readline())
note_arr = list(map(int, sys.stdin.readline().split()))  #적혀져 있는 카드

# out_arr = [0]*M

arr_dic = dict()            #dict형태로 반환

for i in arr:
    if i in arr_dic:
        arr_dic[i] +=1      #arr의 원소를 arr_dic[키] = 개수 형태로 삽입
    else:
        arr_dic[i] = 1      #없다면 1로 삽입
print(arr_dic)
for i in range(M):
    if note_arr[i] in arr_dic:      #적혀져 있는 카드의 i번째 카드가 arr_dic에 있다면
        print(arr_dic[note_arr[i]], end=' ')    #note_arr의 i번째 값의 value값
    else:
        print(0, end=' ')
# for i in range(max(N,M)):                     #counting array 사용
#     if arr[i] in note_arr:
#         out_arr[note_arr.index(arr[i])] +=1
#     else:
#         continue

# for i in range(M):                            #count함수 사용
#     if note_arr[i] in arr:
#         out_arr[i]= arr.count(note_arr[i])
#     else:
#         pass
# print(out_arr)