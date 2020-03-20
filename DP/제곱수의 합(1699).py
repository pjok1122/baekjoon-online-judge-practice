'''
[문제 풀기 전 생각할 것]
1,2,3 더하기 문제와 유사한 문제.

? + ? + ? + ? = N 이 되는 형태인데, 마지막 ?가 i^2이라면, 앞의 물음표 3개를 더한 값은 N-i^2이 된다.

따라서 dp[n] = min(dp[n-i^2]+1)이라고 할 수 있다.
'''

n = int(input())
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = i
    j = 1
    while j*j <= i:
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
        j += 1

print(dp[n])
