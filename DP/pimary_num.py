'''
dp[n] : n자리 이친수의 개수

결국 마지막 자리는 0 또는 1로 끝나게 된다.
만약, 마지막 자리가 0이라면, 앞의 n-1 자리는 n-1자리의 이친수를 그대로 사용할 수 있다.
만약, 마지막 자리가 1이라면, n-1번째 자리는 반드시 0이어야 한다. 따라서 위와 마찬가지로 n-2자리에는 이친수를 그대로 사용할 수 있다.

dp[n] = dp[n-1] + dp[n-2], dp[1] = 1, dp[2] = 1

'''

import sys
sys.setrecursionlimit(10**7)
dp = [0]*1001
dp[1] = 1
dp[2] = 1
#Top-down
def func(n):
    if dp[n]:
        return dp[n]
    
    dp[n] = func(n-1) + func(n-2)
    return dp[n]

n = int(input())
print(func(n))