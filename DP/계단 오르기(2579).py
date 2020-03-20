'''
[문제 풀기 전 생각할 것]

연속해서 3개의 계단을 밟지 못한다는 조건이 있으므로, 연속해서 몇 개의 계단을 밟았는지에 대한 정보를 가지고 있는게 좋다.
dp[i][0] := 연속해서 0개의 계단.
dp[i][1] := 연속해서 1개의 계단.
dp[i][2] := 연속해서 2개의 계단.

dp[i][j] := 계단 i개가 있고, 연속해서 j개의 계단을 밟았을 때, 합계가 가장 높아지는 값.

포도주시식과의 차이점은, 연속해서 2개의 계단을 건너뛸 수 없다는 점이다.
따라서, dp[i][0] = dp[i-1][0] 이어서는 안된다.

dp[i][0] = max(dp[i-1][1], dp[i-1][2])
dp[i][1] = dp[i-1][0] + arr[i]
dp[i][2] = dp[i-1][1] + arr[i]

조심해야 할 예시 : [10 3 2 1 100 100]

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]

dp = [[-1 for col in range(3)] for row in range(n)]

dp[0][0] = 0
dp[0][1] = arr[0]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0]+arr[i]
    dp[i][2] = dp[i-1][1]+arr[i]
print(max(dp[n-1][1], dp[n-1][2]))
