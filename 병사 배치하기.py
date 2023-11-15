# DP - 병사 배치하기
# 이것이 취업을 위한 코딩 테스트다 (380p)

N = int(input())
data = list(map(int, input().split()))

dp = [1 for _ in range(N)]

# 가장 긴 증가하는 부분 수열(LIS, Longest Increasing Subsequence) 알고리즘
#  : 임의의 수열이 주어질 때, 몇 개의 수들을 제거해서 부분수열을 만음 
#    이때 만들어진 부분수열 중 오름차순으로 정렬된 가장 긴 수열
for i in range(1, N):
    for j in range(i):
        if data[i] < data[j]:
						# dp 중 큰 값과 1 더한 값 중 최댓값을 저장
            dp[i] = max(dp[i], dp[j]+1)

# 열외해야 하는 병사의 최소 수 = 전체 - 최장 감소 부분 값
print(len(data) - max(dp))