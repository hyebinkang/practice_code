N = int(input())
time = sorted(list(map(int, input().split())))[:N]      #오름차순으로 정렬한 리스트
minute = 0
total_time = 0

for i in range(N):
    minute += time[i]                                   #각 사람 당 걸리는 시간
    total_time += minute                                #총 걸리는 시간

print(total_time)