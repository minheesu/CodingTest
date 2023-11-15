# 단어사전
# https://www.codetree.ai/training-field/search/problems/word-dict/description?page=1&pageSize=20&tags=String&order=-tier

data = list(set(input().split()))   # 중복 제거
data = sorted(data, reverse=False) # key=lambda x:x[n]

for i in data:
    print(i, end=' ')