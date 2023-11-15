# 대여 연체료
# https://www.codetree.ai/training-field/search/problems/word-flip/description?page=2&pageSize=20&tags=String&order=tier

import sys

rental = {}    # 대여 정보를 저장하는 dict
late_fee = []  # 연체료 정보를 저장하는 list

N, H, M, F = map(int, sys.stdin.readline().split())

total_M = H*60 + M   # 입력된 시간을 분으로 변환

for _ in range(N):
    h, m, p, name = map(str, sys.stdin.readline().split())

    h = int(h)
    m = int(m)

    total_f = 0
    key_name = p+name   # 대여자와 대여물품 이름을 조합한 키 생성

    # 대여 시,
    if key_name not in rental: 
        rental[key_name] = [h,m]  # 대여정보 저장
    # 반납 시,
    else:
        rental_h, rental_m = rental[key_name]
        total_m = (h-rental_h)*60 + (m-rental_m)   # 대여 기간 계산

        # 연체료 계산
        if total_m > total_M:
            total_f = (total_m-total_M) * F
            late_fee.append((name, total_f))   # 연체료 정보 저장

if late_fee:
    # 이름을 기준으로 재정렬
    late_fee = sorted(late_fee, key=lambda x: x[0])

    for name, fee in late_fee:
        print(name, fee)
else:
    print('-1')   # 연체료가 없는 경우 -1 출력