def solution(land):
    answer = 0
    dp = [[0 for col in range(4)] for row in range(len(land))]
    dp[0] = land[0]

    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2],
                           dp[i-1][j-3]) + land[i][j]

    # for i in range(0, len(land)):
    #     print(dp[i])
    # print(max(dp[len(land)-1]))
    return max(dp[len(land)-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
print(solution([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))
print(solution([[1, 1, 1, 1], [1, 1, 1, 2], [
      2, 1, 1, 1], [1, 1, 2, 1], [1, 2, 1, 1]]))

print(solution([[1, 2, 2, 2], [100, 100, 1, 100], [100, 1, 1, 1]]))
