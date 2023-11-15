# 구현 - 기둥과 보 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/60061

def build_check(frame, x, y, types):
    # 기둥인 경우
    if types == 0:
        if y == 0:                      # 바닥 위에 설치 
            return True
        elif (x-1, y, 1) in frame:      # 왼쪽 보 위에 설치
            return True
        elif (x, y, 1) in frame:        # 오른쪽 보 위에 설치
            return True
        elif (x, y-1, 0) in frame:      # 다른 기둥 위에 설치
            return True
        return False
		# 보인 경우
    else :
        if (x, y-1, 0) in frame:        # 왼쪽 기둥 위에 설치
            return True
        elif (x+1, y-1, 0) in frame:    # 오른쪽 기둥 위에 설치
            return True
        elif (x-1, y, 1) in frame:      # 양쪽 보와 연결
            return True
        return False