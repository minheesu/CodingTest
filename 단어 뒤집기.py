# 단어 뒤집기
# https://www.codetree.ai/training-field/search/problems/word-flip/description?page=2&pageSize=20&tags=String&order=tier

N = input()
# N = 'ywfrexgln<knfxypkvcwnvuxmlycmamqs crff>tu<ombelpskukcl opipwkena>ekujvuopurbirwjorkk'

flag = True    # 문자 역순 확인, '<'가 나오면 False '>'가 나오면 True
result = []    # 최종 결과를 저장할 리스트
reverse = []   # '<' 와 '>' 사이의 문자를 역순으로 저장할 리스트

n_len = len(N)
i = 0

for char in N:
    if char == ' ':
				# '<'와 '>' 사이의 문자 역순 추가
        if reverse:
            result.append(reverse[::-1])
            reverse = []
        result.append(char)
    elif char == '<':
				# '<'와 '>' 사이의 문자 역순 추가
        if reverse:
            result.append(reverse[::-1])
            reverse = []
        flag = False
        result.append(char)
    elif char == '>':
        flag = True
        result.append(char)
    # '<'와 '>' 안에 들어가 있는 경우, 입력 그대로 결과에 추가
    elif (char != '>' or char != '<') and not flag:
        result.append(char)
    # '<'와 '>' 안에 들어가 있지 않는 경우, 문자 역순 모드에서 문자 역순으로 저장
    elif (char != '>' or char != '<') and flag:
        reverse.append(char)

    i += 1
    # 문자열이 끝나면 남은 문자 역순 추가
    if i == n_len and reverse:
        result.append(reverse[::-1])
        reverse = []

print(''.join([''.join(_result) if isinstance(_result, list) else _result for _result in result]))