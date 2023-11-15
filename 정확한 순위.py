# 최단경로 - 정확한 순위
# 이것이 취업을 위한 코딩 테스트다 (386p)

n, m = map(int, input().split())

INF = int(1e9)  # 무한을 의미
arr = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(1, m + 1):
  a, b = map(int, input().split())
  arr[a][b] = 1

# 플로이드 워셜 알고리즘 수행;
# 하나의 정점에서 다른 정점까지 바로 갈 수 있으면 최소 비용을, 갈 수 없다면 INF로 배열에 값을 저장
for k in range(1, n + 1):
  for x in range(1, n + 1):
    if x == k:
      continue
    for y in range(1, n + 1):
      if y == k or x == y:
        continue
      arr[x][y] = min(arr[x][y], arr[x][k] + arr[k][y])

# INF는 0으로, 아닌 값은 1로 변경
for x in range(n + 1):
  for y in range(n + 1):
    if arr[x][y] == INF:
      arr[x][y] = 0
    else:
      arr[x][y] = 1

result = 0
for x in range(1, n + 1):
  cnt = 0
  for y in range(1, n + 1):
    cnt += arr[y][x]
  # 본인(n)보다 낮거나 높은 성적의 합이 본인을 포함해 n과 같다면,
  if sum(arr[x]) + cnt == n - 1:
    result += 1

print(result)