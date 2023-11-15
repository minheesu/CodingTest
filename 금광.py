# DP - 금광

# 부모 노드 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


# 두 노드가 속한 집합 합치기
def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n, m = map(int, input().split())      # n : 여행지의 수, m : 도시의 수
parent = list(range(n+1))             # 여행지에 대한 1차원 배열

# 여행지간 연결 정보
for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    # 여행지가 연결되어 있다면, 루트 노드에 맞춰 합치기
    if data[j]:
      union(parent, i, j)

plan = list(map(int, input().split()))  # 여행 계획에 포함된 여행지의 번호

result =  True
# 여행 계획에 속한 모든 노드(여행지)의 루트가 동일한지 확인
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False
        break

print('YES') if result else print('NO')