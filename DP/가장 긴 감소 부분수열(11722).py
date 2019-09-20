'''
가장 긴 증가 부분수열 문제 11053번 문항과 논리가 완벽하게 동일합니다.

다만, 감소하는 수열의 길이이기 때문에, 식이 다음과 같이 살짝 변경됩니다.

DP[i] = max(DP[j]+1) (단, i>j && arr[i]<arr[j])

다른 방법으로는 수열 자체를 뒤집어, LIS문제로 변경해서 풀 수 있습니다.

'''

N = int(input())
arr =list(map(int, input().split()))
arr.reverse()
dp = [0]*(N)

for i in range(N):
    dp[i] = 1

    for j in range(i):
        if arr[i] > arr[j] and dp[i]<dp[j]+1:
            dp[i] = dp[j]+1

print(max(dp))
    