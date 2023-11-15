# 최단 경로 - 숨바꼭질
# 이것이 취업을 위한 코딩 테스트다 (390p)

import heapq

def dijkstra(start):
  distance[start] = 0   # 시작 노드의 최단 거리는 0으로 초기화
  q = []                # 우선순위 큐를 사용하여 노드 탐색 순서 관리
  heapq.heappush(q, (0, start)) # 시작 노드를 우선순위 큐에 추가

  while q:
    dist, node = heapq.heappop(q)
    # 최단 거리일 경우(이미 업데이트가된 경우) 무시하고 다음 노드 탐색
    if dist > distance[node]:
      continue
		# 현재 노드와 연결된 노드들을 순회
    for num, num_d in graph[node]:
      if distance[num] > dist + num_d:
        distance[num] = dist + num_d   # 더 짧은 거리로 업데이트
        heapq.heappush(q, (distance[num], num))   # 업데이트된 노드를 큐에 추가
  return distance


N, M = map(int, input().split())
INF = int(1e9)

start = 1  # 시작 노드는 1번
graph = [[] for i in range(N + 1)]  # 노드에 대한 정보
distance = [INF] * (N + 1)  # 노드별 최단거리 정보

# 간선 정보 저장; 이동 비용은 1
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

# 다익스트라 알고리즘으로 distance 계산
dijkstra(start)

# 최단 거리 리스트 내에 최장 거리를 가지는 노드 찾기
max_dist = max(distance[1:])
max_node = [i for i, dist in enumerate(distance) if dist == max_dist]

print(min(max_node), max_dist, len(max_node), sep=' ')