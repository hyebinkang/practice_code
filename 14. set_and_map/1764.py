n, m = map(int, input().split())    #n: 듣도 못한사람 수, m: 보도 못한 사람 수
arr = {}
union = list()
for _ in range(n):                  #n만큼 arr에 저장
    s = input()
    arr[s] = True

for i in range(m):                  #m만큼 돌고, arr의 key에 a와 입력된 것과 같은 것이 있으면 리스트에 저장
    a = input()
    if a in arr.keys():
        union.append(a)

new_union = sorted(union)           #오름차순으로 정렬
print(len(union))                   #듣보잡의 수
for j in new_union:                 #듣보잡의 명단
    print(j)