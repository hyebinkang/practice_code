from collections import deque

def bfs_maze(maze):
    # 미로의 크기 N x M
    n = len(maze)
    m = len(maze[0])

    # 상, 하, 좌, 우 이동을 위한 좌표 변화량
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 여부를 확인하는 배열
    visited = [[False] * m for _ in range(n)]

    # BFS를 위한 큐, 시작점 (0, 0)
    queue = deque([(0, 0)])
    visited[0][0] = True

    # 출발점에서의 거리 기록 (출발점은 1로 시작)
    distances = [[0] * m for _ in range(n)]
    distances[0][0] = 1

    # BFS 실행
    while queue:
        x, y = queue.popleft()

        # 출구에 도착한 경우, 최단 경로 길이를 반환
        if x == n - 1 and y == m - 1:
            return distances[x][y]

        # 현재 위치에서 4방향으로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로의 범위를 벗어나지 않고, 벽이 아니며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                # 이전 위치의 거리에서 1을 더해 다음 위치의 거리를 기록
                distances[nx][ny] = distances[x][y] + 1

    # 출구에 도달하지 못한 경우 (이 문제에서는 항상 도달 가능하다고 가정)
    return -1


# 입력 예시
maze = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

# 결과 출력
result = bfs_maze(maze)
print(result)
