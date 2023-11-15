# 단어공부
# https://www.acmicpc.net/problem/1157

data = input()

dict = {}
for i in range(len(data)):
  alpha = data[i].upper()

  if alpha in dict:
    dict[alpha] += 1
  else:
    dict[alpha] = 1

max_keys = [key for key, value in dict.items() if value == max(dict.values())]

if len(max_keys) > 1:
  print("?")
else:
  print(max_keys[0])