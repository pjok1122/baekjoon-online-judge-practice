def solution(board):
    dp = [[i for i in row] for row in board]
    answer = 0

    for i in range(1, len(dp)):
        for j in range(1, len(dp)):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            if answer < dp[i][j]:
                answer = dp[i][j]
    

    return answer**2;

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))

