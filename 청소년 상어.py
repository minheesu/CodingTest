# 삼성 기출 - 청소년 상어
# https://www.acmicpc.net/problem/19236

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

fishs = []      # 물고기 value, direction 4X4 배열
fishs_pos = {}  # 물고기 position 리스트


class Fish:

  def __init__(self, num, direction_num):
    self.num = num
    self.dir_num = direction_num

  def get_direction(self):
    return (dx[self.dir_num], dy[self.dir_num])

  # 현재 물고기가 가르키고 있는 위치의 다음 물고기 정보 가져오기
  def get_curr_point_target(self, pos, plus_pos=0):
    # 4X4 범위를 벗어나지 않는 경우
    if 0 <= pos[0] + dx[self.dir_num] < 4 and 0 <= pos[1] + dy[
        self.dir_num] < 4:
      new_pos = self.dir_num + plus_pos
      target_fish = fishs[pos[0] + dx[new_pos]][pos[1] + dy[new_pos]]

      if target_fish.num != -1:
        # 가르키고 있는 물고기의 포지션 return
        return (pos[0] + dx[self.dir_num], pos[1] + dy[self.dir_num])
      else:
        print('This is shark !')
        # TODO: 재귀적으로 찾기
        plus_pos += 1
        return fishs[pos[0]][pos[1]].get_curr_point_target((pos[0], pos[1]), plus_pos)
        # return False
    else:
      print('No path !')
      # TODO: 재귀적으로 찾기
      plus_pos += 1
      return fishs[pos[0]][pos[1]].get_curr_point_target((pos[0], pos[1]), plus_pos)
      # return False


# 물고기 value, direction 4X4 배열 구축
for x in range(4):
  data = list(map(int, input().split()))
  y = 0
  temp = []
  # 입력 데이터를 value, direction 쌍에 맞춰서 재구축
  for i in range(0, len(data), 2):
    temp.append(Fish(data[i], data[i + 1] - 1))
    fishs_pos[data[i]] = (x, y)
    y += 1
  fishs.append(temp)

# 물고기 배열 (0,0)을 상어(-1)로 변경
fishs_pos[-1] = fishs_pos.pop(fishs[0][0].num)
fishs[0][0].num = -1

# 물고기 이동
for fish_num in range(1, 17):
  if fish_num in fishs_pos:
    print(fish_num)
    fish_x, fish_y = fishs_pos[fish_num]  # 해당 번호 물고기의 위치(x, y)
    # 다음 위치의 물고기를 찾기
    target_fish = fishs[fish_x][fish_y].get_curr_point_target((fish_x, fish_y))
    # 다음 위치의 물고기와 서로 위치 이동
    if target_fish:
    #  print(target_fish)
       temp_fish = target_fish
       fishs[target_fish[0]][target_fish[1]] = fishs[fish_x][fish_y]
       fishs[fish_x][fish_y] = temp_fish

# 상어가 이동가능한 위치별 먹은 물고기 더하기

# 최댓값 찾기