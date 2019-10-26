'''
2*n 타일링을 채우는 방법은
2*n-1 타일링을 세우는 방법과 2*n-2 타일링을 세우는 방법을 더해주면 끝.

dp[n] = dp[n-1]+dp[n-2] , dp[0] = 1 dp[1] = 1 로 놓아야 dp[2] = 2가 성립됨. Fibonacci series와 동일한 문제.
'''

import sys
sys.setrecursionlimit(10**7)
dp = [0]*1001
dp[0] = 1
dp[1] = 1
# Top-down


def func(n):
    if dp[n]:
        return dp[n]

    dp[n] = func(n-1) + func(n-2)
    return dp[n]


n = int(input())
print(func(n) % 10007)
