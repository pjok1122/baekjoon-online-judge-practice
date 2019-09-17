
#효율성 테스트, 시간초과 5개 중 3개 발생
def solution(words, queries):
    answer = []
    for query in queries:
        cnt = query.count('?')
        length = len(query)
        start_flag=0
        result = 0

        if query[0] =='?':
            data = query[cnt:]
            start_flag = 0
        else:
            data = query[:-cnt]
            start_flag = 1
        
        for word in words:
            if len(word) != length:
                continue
            if start_flag:           
                if word[:-cnt] == data:
                    result+=1
            else:
                if word[cnt:] == data:
                    result+=1
        answer.append(result)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))