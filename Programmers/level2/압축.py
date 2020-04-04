def solution(msg):
    answer = []
    dic ={}
    for i in range(26):
        dic[chr(ord('A') + i)] = i+1

    next_index = 27
    comp_len = 1
    index = 0
    while(index < len(msg)):
        # 몇 글자까지 압축할 수 있는지 검사.
        comp_len = 1
        while(index + comp_len <= len(msg)):
            if(msg[index:index+comp_len] in dic.keys()):
                comp_len+=1
                continue
            else:
                # 사전에 추가.
                dic[msg[index:index+comp_len]] = next_index
                next_index+=1

                # 정답에 색인 추가
                answer.append(dic[msg[index:index+comp_len-1]])
                index += comp_len-1
                comp_len = 1
                break
        
        # 마지막 글자까지 압축이 가능한 경우.
        if(index + comp_len > len(msg) and comp_len > 1):
            if(index>=len(msg)):
                break
            answer.append(dic[msg[index:]])
            break
    return answer

# print(solution("KAKAO"))
# print(solution("ABCDEFGHIJK"))
# print(solution("AZ"))
print(solution("ABABCABZABC"))