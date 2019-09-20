'''
가장 긴 증가 부분수열 문제 11053번 문항과 논리가 완벽하게 동일합니다.

다만, 수열의 길이가 수의 합으로 변경되었을 뿐입니다.
'''

N = int(input())
arr =[0]+list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = arr[i]

    for j in range(1,i):
        if arr[i] > arr[j] and dp[i]<dp[j]+arr[i]:
            dp[i] = dp[j]+arr[i]

print(max(dp))