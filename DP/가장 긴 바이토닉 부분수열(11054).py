'''
[LIS의 응용문제]

dp[i] = LIS[i] + rev_LIS[N-i-1] - 1

'''

N = int(input())
arr = list(map(int, input().split()))
arr2 = arr[::-1]

LIS = [1]*N
rev_LIS = [1]*N
dp = [1]*N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and LIS[i] < LIS[j]+1:
            LIS[i] = LIS[j]+1

for i in range(N):
    for j in range(i):
        if arr2[i] > arr2[j] and rev_LIS[i] < rev_LIS[j]+1:
            rev_LIS[i] = rev_LIS[j]+1

for i in range(N):
    dp[i] = LIS[i]+rev_LIS[N-i-1]-1

print(max(dp))
