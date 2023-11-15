# 삼성 - 마법사 상어와 파이어볼
# https://www.acmicpc.net/problem/20056

from collections import deque

N, M, K = map(int, input().split())
que = deque()
arr = [[deque() for _ in range(N)] for _ in range(N)]

# 2차원 배열에 파이어볼의 질량, 속도, 방향 정보를 리스트 형태로 저장
for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  arr[r - 1][c - 1].append([m, s, d])
  que.append([r - 1, c - 1])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

fireballs = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(K):
  # 파이어볼 이동
  for _ in range(len(que)):
    x, y = que.popleft()
    for _ in range(len(arr[x][y])):
      _m, _s, _d = arr[x][y].popleft()
			# 1번과 N번 행은 연결되어 있으므로, _d방향으로 _s만큼 이동 후 N과 나머지 연산
      _r = (_s * dx[_d] + x) % N  
      _c = (_s * dy[_d] + y) % N  
      fireballs[_r][_c].append([_m, _s, _d])

  # 칸마다 파이어볼이 2개 이상 들어있는지 확인
  for r in range(N):
    for c in range(N):
      # 파이어볼이 1개인 경우, 바로 append
      if len(fireballs[r][c]) == 1:
        fireballs.append([r, c] + fireballs[r][c].pop())

      # 파이어볼이 2개 이상인 경우, 4개의 파이어볼로 쪼개기
      else:
        sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(fireballs[r][c])
        while fireballs[r][c]:
          _m, _s, _d = fireballs[r][c].pop(0)
          sum_m += _m
          sum_s += _s
					# 방향 정보가 홀수라면
          if _d % 2:
            cnt_odd += 1
					# 방향 정보가 짝수라면
          else:
            cnt_even += 1

        # 질량이 0일 경우, 소멸
        if sum_m // 5:
          # 방향이 모두 홀수이거나 짝수인 경우
          if cnt_odd == cnt or cnt_even == cnt: dir = [0, 2, 4, 6]
          else: dir = [1, 3, 5, 7]

          for d in dir:
            fireballs.append([r, c, sum_m // 5, sum_s // cnt, d])

# 질량 합계
result = 0
for i in fireballs:
  if i[2]: result += i[2]
print(result)