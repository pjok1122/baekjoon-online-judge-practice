def solution(s):
    Min = 100000
    answer =''
    if len(s)==1:
        return 1
    for i in range(1, len(s)//2 +1):
        j=i
        now = s[:i]
        String =''
        while(j<len(s)):
            cnt = 1
            while (j<len(s) and s[j:j+i] == now):
                cnt+=1
                j+=i
            if cnt==1:
                String += now
            else:
                String += str(cnt)+ now

            now = s[j:j+i]
            j+=i

        String += now
        if len(String) < Min:
            answer = String
            Min = len(String)

    return len(answer)

print(solution("a"))

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))

