N, M = map(int, input().split())

arr = []
new_arr = []

def back(start):

    if len(arr) == M:                   #배열에 저장된 길이가 M과 같으면
        print(' '.join(map(str,arr)))   #문자로 변환하여, 공백을 넣고 join한 것을 출력
        return

    for i in range(start, N+1):
        if i not in arr:
            arr.append(i)
            back(i+1)
            arr.pop()
back(1)



