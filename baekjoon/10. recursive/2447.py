n = int(input())

def star(l):
    if l==3:
        return ['***', '* *', '***']        #한개의 모양

    arr = star(l//3)                        #n=l, n은 3의 제곱수
    stars = []                              #for에서 추가되는 별의 모양 저장

    for i in arr:                           #첫째모양
        stars.append(i*3)

    for i in arr:                           #중간모양
        stars.append(i+' '*(l//3)+i)

    for i in arr:                           #마지막모양
        stars.append(i*3)

    return stars

print('\n'.join(star(n)))                   #줄바꿈을 넣어서 문자열 합치기