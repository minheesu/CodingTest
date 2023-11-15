# 집합
# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline
M = int(input())
S = set()

for _ in range(M):
  data = list(input().split())
  cal = data[0]

  if cal == 'all':
    S = set([i for i in range(1, 21)])
  elif cal == 'empty':
    S = set()
  elif cal == 'add':
    S.add(int(data[1]))
  elif cal == 'remove':
    S.discard(int(data[1]))
  elif cal == 'check':
    print(1 if int(data[1]) in S else 0)
  elif cal == 'toggle':
    if int(data[1]) in S:
      S.discard(int(data[1]))
    else:
      S.add(int(data[1]))