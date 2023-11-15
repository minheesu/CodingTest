# DFS/BFS - 유기농 배추
# https://www.acmicpc.net/problem/1012

# 필수 ! 파이썬의 기본 재귀 깊이 제한은 1000 임으로 제한 늘리기
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  # 상하좌우로 이동 가능
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < m) and (0 <= ny < n):
      if data[ny][nx] == 1:
        data[ny][nx] = 0
        dfs(nx, ny)

for _ in range(int(input())):
  m, n, k = map(int, input().split())
  data = [[0] * n for _ in range(m)]

  # 배추밭. 0: 배추가 심어져 있지 않은 땅, 1: 배추가 심어져 있는 땅
  for _ in range(k):
    x, y = list(map(int, input().split()))
    data[x][y] = 1

  result = 0
  for i in range(n):
    for j in range(m):
      # 배추가 심어져 있으면 cnt
      if data[i][j] != 0:
        dfs(i, j)
        result += 1

  print(result)