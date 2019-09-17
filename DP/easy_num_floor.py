'''
dp[n][l] : 마지막 자리수가 l인 n자리 계단수의 갯수

dp[n][l] = dp[n-1][l-1] + dp[n-1][l+1] ( 1<=l<=8 )
dp[n][l] = dp[n-1][l-1] ( l ==9 )
dp[n][l] = dp[n-1][l+1] ( l ==0 )

정답 : sigma(dp[n][l]) 0 to 9
'''
n = int(input())

dp=[[0 for col in range(10)] for row in range(101)]
dp[1][0] = 0
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for l in range(0, 10):
        if(l>0):
            dp[i][l] += dp[i-1][l-1]
        if(l<9):
            dp[i][l] += dp[i-1][l+1]
        dp[i][l] %= 1000000000

result =0
for l in range(0,10):
    result += dp[n][l]

print(result%1000000000)
