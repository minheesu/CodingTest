# 이진탐색 - 정렬된 배열에서 특정 수의 개수 구하기
# 이것이 취업을 위한 코딩 테스트다 (267p)

# data 에서 target의 첫번째 인덱스 찾기
def binary_search_first_index(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      if mid - 1 < 0 or arr[mid - 1] != target:
        return mid
      else:
        end = mid - 1
    elif arr[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1

  return -1


# data 에서 target의 마지막 인덱스 찾기
def binary_search_last_index(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      if mid + 1 >= len(arr) or arr[mid + 1] != target:
        return mid
      else:
        start = mid + 1
    elif arr[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1

  return -1


n, target = map(int, input().split())
data = list(map(int, input().split()))

start_index = binary_search_first_index(data, target, 0, n - 1)
end_index = binary_search_last_index(data, target, 0, n - 1)

if start_index == -1:
  print(-1)
else:
  print(end_index - start_index + 1)