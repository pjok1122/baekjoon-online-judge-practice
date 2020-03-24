def solution(s):
    answer = len(s)
    for size in range(1, len(s)//2+1):
        before = s[:size]
        after = ''
        count = 1
        answer_str = ''
        for i in range(size, len(s), size):
            after = s[i:i+size]
            if (before == after):
                count += 1
            else:
                if(count > 1):
                    answer_str += str(count)
                answer_str += before
                before = after
                count = 1
        if count>1:
            answer_str += str(count)
            answer_str += after
        else:
            answer_str += s[i:]

        if answer > len(answer_str):
            answer = len(answer_str)
    return answer    
solution("aabbaccc")
solution("ababcdcdababcdcd")
