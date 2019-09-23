##  Dynamic Programming

 DP는 이미 계산된 결과를 다시 계산하지 않도록, 메모리에 값을 저장해두는 프로그래밍 기법입니다.

 Bottom-up(Iterative), Top-down(Recursive) 방식이 존재하지만, 두 방식 중 하나라도 잘 구현할 수 있으면 됩니다.

 1. DP의 핵심은 배열이 갖는 의미를 명확히 정의하는 것입니다.
 
 ex) dp[n] := n이 숫자 1이 될 때까지 필요한 연산의 최소 횟수

 2. DP 자체만으로 문제를 출제하는 경우는 많지 않습니다. BFS와 연계된 문제에 집중하세요.


## 기본 소스 코드

```python

# 배열의 초기값 지정
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
