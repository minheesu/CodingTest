# 이진 탐색 - 가사 검색
# https://school.programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    answer = []
    
    # queries 안의 문자열을 하나씩 비교
    for query in queries:
        # query 길이와 각 word 길이를 우선적으로 비교하기 위함
        query_len = len(query)
        
        # query 내 '?' 개수 세기
        count_marks = 0
        for char in query:
            if char == '?':
                count_marks += 1
        
        search_query = ''
        cnt = 0
        for word in words:
            word_len = len(word)
            # 접두사에 '?'가 포함될 경우
            if query[0] == '?':
                # query의 접두사에 포함된 '?' 자르기 
                search_query = query[count_marks:]
                # 기존 query 길이와 word 길이가 같고, search_query와 word가 같은 경우, 포함
                if query_len == word_len and word[count_marks:] == search_query:
                    cnt += 1
            # 접미사에 '?'가 포함될 경우
            elif query[-1] == '?':
                # query의 접미사에 포함된 '?' 자르기 
                search_query = query[:-count_marks]
                # 기존 query 길이와 word 길이가 같고, search_query와 word가 같은 경우, 포함
                if query_len == word_len and word[:-count_marks] == search_query:
                    cnt += 1
    
        answer.append(cnt)
        
    return answer