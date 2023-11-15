# 벌집
# https://www.acmicpc.net/problem/2292

n = int(input())

num_beehive = 1  
cnt = 1
while n > num_beehive :
  num_beehive += 6 * cnt  # 벌집 6의 배수로 증가
  cnt += 1  
  
print(cnt)