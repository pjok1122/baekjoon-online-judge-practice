'''
2*n 타일링을 채우는 방법은
2*n-1 타일링을 놓는 방법 + (2*n-2 타일링을 놓는 방법 * 놓을 수 있는 방법이 2가지) 이므로,

dp[n] = dp[n-1]+2*dp[n-2] , dp[0] = 1 dp[1] = 1 로 놓아야 dp[2] = 2가 성립됨.
'''

import sys
sys.setrecursionlimit(10**7)
dp = [0]*1001
dp[0] = 1
dp[1] = 1
#Top-down
def func(n):
    if dp[n]:
        return dp[n]
    
    dp[n] = func(n-1)+2*func(n-2)
    return dp[n]

n = int(input())
print(func(n)%10007)