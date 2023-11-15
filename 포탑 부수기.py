# 삼성 - 포탑 부수기
# https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret/description?page=1&pageSize=20

import sys
from collections import deque


def find_attack():
  power = 5001
  x = y = 0
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 0:
        continue
      if arr[i][j] < power:
        power = arr[i][j]
        x, y = i, j
      elif arr[i][j] == power:
        if attack_time[i][j] > attack_time[x][y]:
          x, y = i, j
        elif attack_time[i][j] == attack_time[x][y]:
          if i + j > x + y:
            x, y = i, j
          elif i + j == x + y:
            if j > y:
              x, y = i, j
  return x, y

def find_target(ax, ay):
  power = -1
  x = y = 0
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 0:
        continue
      if i == x and j == y:
        continue
      if arr[i][j] > power:
        power = arr[i][j]
        x, y = i, j
      elif arr[i][j] == power:
        if attack_time[i][j] < attack_time[x][y]:
          x, y = i, j
        elif attack_time[i][j] == attack_time[x][y]:
          if i + j < x + y:
            x, y = i, j
          elif i + j == x + y:
            if j > y:
              x, y = i, j
  return x, y

def laser_attack(ax, ay, tx, ty):
  attack_point = arr[ax][ay]
  arr[tx][ty] -= attack_point

  q = deque()
  q.append((ax, ay, []))  # x, y, path
  visited = [[False] * M for _ in range(N)]
  visited[ax][ay] = True

  while q:
    x, y, path = q.pop()
    if (x, y) == (tx, ty):
        return True

    for i in range(4):
        nx = (x + dx[i]) % N
        ny = (y + dy[i]) % M
        if arr[nx][ny] != 0 and not visited[nx][ny]:
            new_path = path + [(nx, ny)]
            visited[nx][ny] = True
            q.appendleft((nx, ny, new_path))

        if nx == tx and ny == ty:
            arr[nx][ny] -= attack_point
            for rx, ry in new_path:
                arr[rx][ry] -= attack_point // 2
                attack[rx][ry] = True
            return True 

  return False  # 최단 경로가 존재하지 않는 경우, FALSE

def shell_attack(ax, ay, tx, ty):
  attack_point = arr[ax][ay]
  arr[tx][ty] -= attack_point

  for i in range(8):
    nx = (tx + dx[i]) % N
    ny = (ty + dy[i]) % M
    if nx == ax and ny == ay:
      continue
    arr[nx][ny] -= attack_point // 2

def break_check():
  for x in range(N):
    for y in range(M):
      if arr[x][y] < 0:
        arr[x][y] = 0

def turret_check():
  for x in range(N):
    for y in range(M):
      if arr[x][y] != 0:
        continue
      if attack[x][y]:
        continue
      arr[x][y] += 1


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 포탑 정보 NxM
attack_time = [[0] * M for _ in range(N)]  # 공격 시점 정보; 클수록 최근 포탑, 작을수록 오래된 포탑

# 레이저 공격 위치 (우하좌상 + 대각선)
dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]

for _k in range(K):
  attack = [[False] * M for _ in range(N)]  # 공격 여부

  # 공격자 선정
  attack_x, attack_y = find_attack()
  arr[attack_x][attack_y] += N + M
  attack_time[attack_x][attack_y] = _k + 1
  attack[attack_x][attack_y] = True

  # 공격자의 공격
  target_x, target_y = find_target(attack_x, attack_y)
  attack[target_x][target_y] = True

  # 레이저 공격 시도 후, 안된다면 포탄 공격
  if not laser_attack(attack_x, attack_y, target_x, target_y):
    shell_attack(attack_x, attack_y, target_x, target_y)

  # 포탑 부서짐
  break_check()

  # 포탑 정비
  turret_check()

print(max(map(max, arr)))