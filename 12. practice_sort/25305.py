n, k = map(int, input().split())            #n: 개수, k: 등수 인원

score = sorted(list(map(int, input().split())))     #점수를 리스트로, 정렬하며 받기
score.reverse()                                     #역순으로 배열
print(min(score[:k]))                               #k번째 까지 중에서 가장 작은 값 출력