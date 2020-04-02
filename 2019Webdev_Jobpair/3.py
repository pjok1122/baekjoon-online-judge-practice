sticker = [12, 12, 12, 12, 12]
dp = [[0 for col in range(2)] for row in range(len(sticker))]

dp[0][1] = sticker[0]
dp[0][0] = 0

for i in range(1, len(sticker)):
    dp[i][1] = dp[i-1][0] + sticker[i]
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])

print(max(dp[len(sticker)-1][0], dp[len(sticker)-1][1]))
