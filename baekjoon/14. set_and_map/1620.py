import sys

n, m = map(int, sys.stdin.readline().split())
arr = {}

for _ in range(n):
    put = sys.stdin.readline().strip()
    arr[put] = _                        #arr의 key: 포켓몬 이름, value: 포켓몬 번호
print(arr)
arr_keys = list(arr.keys())             #arr의 key 값 만을 가지는 리스트를 생성
print(arr_keys)
for i in range(m):
    answer = sys.stdin.readline().strip()   #이름, 숫자를 입력할 때
    if answer.isdigit():                    #숫자이면 key값만 있는 arr_keys에서 해당하는 리스트
        print(arr_keys[int(answer)-1])
    else:
        print(arr[answer]+1)