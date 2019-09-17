'''
DP 기본문제.
1. dp[n] = n을 1로 만드는데 드는 최소 연산 횟수
2. BFS를 이용해서도 문제를 풀 수 있다.

'''

import sys
from collections import deque
sys.setrecursionlimit(10**6)

dp = [0]*(10**6+1)

# dp[X]=min(makeZero(X/3)+1, makeZero(X/2)+1, makeZero(X-1)+1)    

# Top - down approach (파이썬 메모리 소요가 너무 큼.)
def makeZero(X):
    if X==3 or X==2:
        return 1
    if X==1:
        return 0
    
    if dp[X]:
        return dp[X]
    
    tmp=[]
    if X%3 ==0:
        tmp.append(makeZero(X//3)+1)
    if X%2 ==0:
        tmp.append(makeZero(X//2)+1)
    tmp.append(makeZero(X-1)+1)
    
    dp[X] = min(tmp)
    return dp[X]

#Bottom-Up approach
def makeZero2(X):
    dp[1] = 0
    
    for i in range(2, X+1):
        dp[i] = dp[i-1] + 1
        if i%2==0 and dp[i] > dp[i//2]+1:
            dp[i] = dp[i//2]+1
        if i%3 ==0 and dp[i] > dp[i//3]+1:
            dp[i] = dp[i//3]+1
    
    return dp[X]

#BFS approach
def makeZero3(X):
    dp[1] = 0
    q = deque()
    q.append(1)
    
    while q:
        v = q.popleft()
        if v == X:
            return dp[v]
        if v+1 <= X and dp[v+1]==0:
            dp[v+1] = dp[v] + 1
            q.append(v+1)
        if 2*v <= X and dp[2*v]==0:
            dp[2*v] = dp[v] + 1
            q.append(2*v)
        if 3*v <= X and dp[3*v]==0:
            dp[3*v] = dp[v] + 1        
            q.append(3*v)

N = int(input())
print(makeZero3(N))