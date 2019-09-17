'''
dp[N][L] := N자리 오르막수 중 마지막 숫자가 L인 수들의 갯수

- dp[N][L] = sig(dp[N-1][k]) (0<=k<=L)

'''
n = int(input())

dp = [[0 for col in range(10)] for row in range(1001)]

for i in range(0,10):
    dp[1][i] = 1

for i in range(1, n+1):
    for j in range(0,10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 10007

result=0
for i in range(10):
    result+=dp[n][i]

print(result%10007)