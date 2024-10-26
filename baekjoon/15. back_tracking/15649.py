N, M = map(int, input().split())

arr = []

def back():
    if len(arr) == M:                   #배열에 저장된 길이가 M과 같으면
        print(' '.join(map(str,arr)))   #문자로 변환하여, 공백을 넣고 join한 것을 출력
        return

    for i in range(1, N+1):             #1~N+1까지
        if i in arr:                    #i가 arr안에 있으면 continue
            continue
        arr.append(i)                   #i저장
        back()                          #다시 처음부터-> if문으로
        arr.pop()                       #if문에서 출력한 이후 arr에 pop시킴

back()