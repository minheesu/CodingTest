# 삼성 - 메이즈 러너
# https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=1&pageSize=20

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]   # 미로 N x N

persons = []     # 참가자의 좌표
for _ in range(M):
  x, y = map(int, input().split())
  persons.append([x - 1, y - 1])  

exit = list(map(int, input().split()))
exit[0] -= 1
exit[1] -= 1

board[exit[0]][exit[1]] = -1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


result = 0   # 모든 참가자의 이동거리 합
for _ in range(K):
    # 모든 참가자가 한 칸씩 이동
    person_exited = []
    for m in range(len(persons)):
        x, y = persons[m]
        flag = abs(x-exit[0]) + abs(y-exit[1])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 or board[nx][ny] == -1:
                    if abs(nx-exit[0]) + abs(ny-exit[1]) < flag:
                        result += 1
                        persons[m] = [nx, ny]
                        break 

    while True:
        if [exit[0], exit[1]] not in persons: 
          break
        else: 
          persons.remove([exit[0], exit[1]])

    # 모든 참가자가 탈출했다면 종료
    if len(persons) == 0: break 
                    
    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
    ex, ey = exit[0], exit[1]
    square = []
    for m in range(len(persons)):
        x, y = persons[m]
        minX = min(x, ex); minY = min(y, ey)
        maxX = max(x, ex); maxY = max(y, ey)

        width = maxY - minY
        height = maxX - minX
        diff = width - height

        if diff == 0: 
          square.append((maxX-minX, minX, minY, maxX, maxY))
          continue
        elif diff > 0: # x 방향 늘리기
            for i in range(abs(diff)):
                if 0 < minX: 
                  minX -= 1
                else: 
                  maxX += 1
        else: # y 방향 늘리기
            for i in range(abs(diff)):
                if 0 < minY: 
                  minY -= 1
                else: 
                  maxY += 1
        square.append((maxX-minX, minX, minY, maxX, maxY))
    square.sort()
    minX, minY, maxX, maxY = square[0][1:]

    # 미로 회전
    S = maxY - minY + 1
    sqr = [[0]*S for s in range(S)]
    for i in range(minX, maxX+1):
        for j in range(minY, maxY+1):
            sqr[i-minX][j-minY] = board[i][j]

    # 참가자 및 출구 회전
    for m in range(len(persons)): 
        x, y = persons[m]
        if minX <= x <= maxX and minY <= y <= maxY:
            tmp = [[0]*S for s in range(S)]
            tmp[x-minX][y-minY] = 1
            tmp = reversed(tmp)
            tmp = list(map(list, zip(*tmp)))

            for i in range(minX, maxX+1):
                for j in range(minY, maxY+1):
                    if tmp[i-minX][j-minY] == 1: persons[m] = [i, j]

    sqr = reversed(sqr)
    sqr = list(map(list, zip(*sqr)))

    for i in range(minX, maxX+1):
        for j in range(minY, maxY+1):
            if sqr[i-minX][j-minY] >= 1:
                board[i][j] = sqr[i-minX][j-minY] - 1
            elif sqr[i-minX][j-minY] == -1:
                board[i][j] = -1
                exit = [i, j]
            else:
                board[i][j] = 0

# 모든 참가자들의 이동 거리 합과 출구 좌표 출력
print(result); print(exit[0]+1, exit[1]+1)