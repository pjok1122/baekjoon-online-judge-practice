'''
1. dp[n][m] := A[0] ~A[n]의 포도주가 있을 때, 현재 연속으로 마신 잔의 수는 m이다. 이 때 포도주 양이 최대가 되도록 설정된 값.
 - dp[n][0] := max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
 - dp[n][1] := dp[n-1][0] + p[n]
 - dp[n][2] := dp[n-1][1] + p[n]

2. 최대 포도주 = max(dp[n][0], dp[n][1], dp[n][2])가 된다.
'''

import sys
import pprint as pp

n = int(input())
p =[0]
dp = [[0 for col in range(3)] for row in range(10001)]

for i in range(n):
    p.append(int(sys.stdin.readline()))

dp[1][0] = 0
dp[1][1] = p[1]
for i in range(2, n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + p[i]
    dp[i][2] = dp[i-1][1] + p[i]
    # print(max(dp[i][0], dp[i][1], dp[i][2]))

print(max(dp[n][0], dp[n][1], dp[n][2]))