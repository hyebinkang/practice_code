import heapq


def dijkstra(graph, start):
    INF = 1e9
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

def delay_time(arr, n, k):
    graph = {}

    for u, v, w in arr:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    Q = [(0, k)]
    dist = {}

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            if node in graph:
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

    if len(dist) == n:
        return max(dist.values())

    return -1


def fibo(n):
    if n in [1, 2]:
        return 1
    return fibo(n-1) + fibo(n-2)

memo = {1: 1, 2: 1}


def fibo_dp(n):
    if n in memo:
        return memo[n]
    memo[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return memo[n]