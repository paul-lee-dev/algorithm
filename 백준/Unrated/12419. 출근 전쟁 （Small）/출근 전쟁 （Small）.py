import heapq
from collections import defaultdict

def calculate_expected_time(S, R, D, P):
    expected_time = R
    if P == 100:
        return float('inf')  # 항상 지연되는 경우, 무한대 시간 소요
    p = P / 100.0
    expected_delay = D * p / (1 - p)
    return expected_time + expected_delay

def dijkstra(N, M, H, O, routes):
    graph = defaultdict(list)
    for A, B, S, R, D, P in routes:
        expected_time = calculate_expected_time(S, R, D, P)
        if expected_time != float('inf'):
            graph[A].append((B, S, expected_time))

    pq = [(0, H)]  # (expected_time, node)
    dist = [float('inf')] * N
    dist[H] = 0

    while pq:
        current_time, current_node = heapq.heappop(pq)

        if current_node == O:
            return current_time

        if current_time > dist[current_node]:
            continue

        for next_node, departure_time, travel_time in graph[current_node]:
            wait_time = (departure_time - current_time % 60) % 60
            next_time = current_time + wait_time + travel_time

            if next_time < dist[next_node]:
                dist[next_node] = next_time
                heapq.heappush(pq, (next_time, next_node))

    return -1  # 목적지에 도달할 수 없는 경우

def solve_case(case_num):
    N, M, H, O = map(int, input().split())
    routes = []
    for _ in range(M):
        A, B, S, R, D, P = map(int, input().split())
        routes.append((A, B, S, R, D, P))

    result = dijkstra(N, M, H, O, routes)
    
    if result == -1:
        print(f"Case #{case_num}: -1")
    else:
        print(f"Case #{case_num}: {result:.7f}")

T = int(input())
for case in range(1, T + 1):
    solve_case(case)