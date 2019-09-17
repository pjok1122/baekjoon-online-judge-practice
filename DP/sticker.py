'''
마지막 스티커의 상태를 나타내보자.

1) 스티커를 떼지 않는다.
2) 위의 스티커를 뗀다.
3) 아래 스티커를 뗀다.

각각을 0,1,2로 매핑하면 다음과 같은 배열을 생각할 수 있다.

dp[N][S] := 2*N 스티커에서 마지막 스티커 상태가 S일 때, 최댓값을 의미한다.

따라서 2*N 스티커로 만들 수 있는 최댓값은 max(dp[N][0], dp[N][1], dp[N][2]) 이다.

이 때, dp[N][0], dp[N][1], dp[N][2]는 다음과 같은 방식으로 구할 수 있다.
dp[N][0] = max(dp[N-1][1], dp[N-1][2]))
dp[N][1] = max(dp[N-1][2], dp[N-1][0]) + P[0][N]
dp[N][2] = max(dp[N-1][1], dp[N-1][0]) + P[1][N]

'''

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    P=[]
    P.append([0] + list(map(int, input().split())))
    P.append([0] + list(map(int, input().split())))
    
    
    dp = [[0 for col in range(3)] for row in range(100001)]

    dp[1][0] = 0
    dp[1][1] = P[0][1]
    dp[1][2] = P[1][1]
    for i in range(1,n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = max(dp[i-1][2], dp[i-1][0]) + P[0][i]
        dp[i][2] = max(dp[i-1][1], dp[i-1][0]) + P[1][i]
    
    result = max(dp[n][0], dp[n][1], dp[n][2])
    print(result)