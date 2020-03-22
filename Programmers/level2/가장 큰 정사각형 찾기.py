def solution(board):
    dp = [[num for num in row] for row in board]
    answer = 0
    if dp[0][0]:
        answer = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if dp[i][j] == 0:
                continue
            
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            if answer < dp[i][j]:
                answer = dp[i][j]

    return answer**2;

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))