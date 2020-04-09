from collections import deque

def solution(n, number):
    MAX_NUM = 10000
    dp = [MAX_NUM] * 32001
    que = deque()
    que.append(n)
    que.append(n*11)
    que.append(n*111)
    que.append(n*1111)

    dp[n] = 1
    dp[n*11] = 2
    dp[n*111] = 3
    dp[n*1111] = 4
    if n*11111 <= 32000:
        dp[n*11111] = 5
        que.append(n*11111)
    while que:
        num = que.popleft()

        if(dp[num]>8):
            continue

        # 곱하기 n
        if num*n<len(dp) and dp[num*n] > dp[num] + 1:
            que.append(num*n)
            dp[num*n] = dp[num] + 1
        
        # 나누기 n
        if (num//n)<len(dp) and dp[num//n] > dp[num] + 1:
            que.append(num//n)
            dp[num//n] = dp[num] + 1
        # 더하기 n
        if num+n<len(dp) and dp[num+n] > dp[num] + 1:
            que.append(num+n)
            dp[num+n] = dp[num] + 1
        
        if num-n>0 and dp[num-n] > dp[num] + 1:
            que.append(num-n)
            dp[num-n] = dp[num] + 1
        
    return dp[number] if dp[number]<=8 else -1

# print(solution(5, 12))
# print(solution(2, 11))
print(solution(4,17))
# print(solution(5,3600))