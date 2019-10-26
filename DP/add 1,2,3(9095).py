'''
dp[n] := n을 1,2,3의 합으로 표현하는 방법의 수
n을 1,2,3의 합으로 표현하는 방법은

1) n-1을 표현하고 + 1을 붙여주는 경우
2) n-2를 표현하고 + 2을 붙여주는 경우
3) n-3을 표현하고 + 3을 붙여주는 경우
이렇게 세가지로 나뉜다

따라서
dp[n] = dp[n-1] + dp[n-2] + dp[n-3] (dp[1]=1, dp[2] =2, dp[3]=4) 로 나타낸다.
'''
dp = [0]*12
dp[1] = 1 
dp[2] = 2
dp[3] = 4
def func(n):
    if dp[n]:
        return dp[n]
    
    dp[n] = func(n-1)+func(n-2)+func(n-3)
    
    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(func(n))