##  Dynamic Programming

 DP는 이미 계산된 결과를 다시 계산하지 않도록, 메모리에 값을 저장해두는 프로그래밍 기법입니다.

 Bottom-up(Iterative), Top-down(Recursive) 방식이 존재하지만, 두 방식 중 하나라도 잘 구현할 수 있으면 됩니다.

 1. DP의 핵심은 배열이 갖는 의미를 명확히 정의하는 것입니다.
 
 ex) dp[n] := n이 숫자 1이 될 때까지 필요한 연산의 최소 횟수

 2. DP 자체만으로 문제를 출제하는 경우는 많지 않습니다. BFS와 연계된 문제에 집중하세요.
 
 3. 2차원 dp를 정의하여 사용하는 것이 더 좋은 결과를 낳을 수도 있습니다.

 ex) dp[N][L] := N자리 오르막수 중 마지막 숫자가 L인 수들의 갯수


## 기본 소스 코드

```python

# 배열의 초기값 지정 (1차원 dp)
dp = [0]*1001
dp[0] = 1
dp[1] = 1

#Top-down
def func(n):
    if dp[n]:
        return dp[n]
    
    dp[n] = func(n-1) + func(n-2)
    return dp[n]

n = int(input())
print(func(n))
```

```python
#2차원 dp 예시 코드
n = int(input())

dp=[[0 for col in range(10)] for row in range(101)]
dp[1][0] = 0
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for l in range(0, 10):
        if(l>0):
            dp[i][l] += dp[i-1][l-1]
        if(l<9):
            dp[i][l] += dp[i-1][l+1]
        dp[i][l] %= 1000000000

result =0
for l in range(0,10):
    result += dp[n][l]

print(result%1000000000)
```