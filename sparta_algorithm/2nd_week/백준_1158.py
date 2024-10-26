def yose(N,K):
    num = K-1                               # K번째 -> 0부터 세야하니까 -1
    num_list = [i for i in range (1,N+1)]   # 1~N+1 까지 리스트 생성
    result = []
    for i in range(N):
        if len(num_list) == 1:              # 마지막 1개 남았을 때
            result.append(num_list[0])      # result에 저장 후 종료
            break
        result.append(num_list[num])        # num번째에 해당하는 수를 저장
        num_list.remove(num_list[num])      # 저장 한 후에는 제거
        num += K-1                          # 원래 이동해야 하는 수 K, 제거한 수 1

        if num >= len(num_list):            # 전체 리스트의 숫자 길이를 세야함
            num %= len(num_list)            # 나머지를 활용

    return result

N, K = map(int, input().split())
result = yose(N,K)
print(f"<{', '.join(map(str, result))}>")

# deque
from collections import deque

def yoses(N,K):
    people = deque(range(1, N+1))
    result = []

    # 큐를 이용해 K번째 사람 제거
    while people:
        people.rotate(-(K-1))   # K-1 번 만큼, 왼쪽으로 땡겨주는거
        result.append(people.popleft())

    print(f"<{', '.join(map(str, result))}>")