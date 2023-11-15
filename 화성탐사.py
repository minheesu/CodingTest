# 최단경로 - 화성탐사
# 이것이 취업을 위한 코딩 테스트다 (388p)

import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
INF = int(1e9)

for _ in range(T):
  N = int(input())
  graph = []
  for _ in range(N):
    graph.append(list(map(int, input().split())))
  distance = [[INF] * N for i in range(N)]

  x, y = 0, 0
  q = [(graph[x][y], x, y)]
  distance[x][y] = graph[x][y]

  while q:
    dist, hx, hy = heapq.heappop(q)
    if distance[hx][hy] < dist:
      continue
    for i in range(4):
      nx = hx + dx[i]
      ny = hy + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, nx, ny))

  print(distance[N - 1][N - 1])