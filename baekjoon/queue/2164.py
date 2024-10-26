from collections import deque

N = int(input())
card = deque([_ for _ in range(1, N+1)])        #deque 안 list선언

while len(card) >1:                             #전체 길이가 1일 때 까지
    card.popleft()                              #맨 앞 제거
    card.append(card.popleft())                 #맨 앞의 것을 다시 뒤로

print(card[0])                                  #남은 것 출력