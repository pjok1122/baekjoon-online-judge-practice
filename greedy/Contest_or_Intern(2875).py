'''
문제 : 팀을 구성할 때는 반드시 여자 2명과 남자 1명으로 구성된다. 가장 많은 팀을 구성하는 것이 문제.
      하지만, 인턴직으로 근무해야하는 사람 수(K)는 반드시 보장해주어야 한다.

1. 남은 사람의 수가 K보다 작아지지 않도록 팀을 구성하면 끝.
2. 시간 복잡도 O(n). 코드 개선 시 O(1)도 가능하다.

'''

N,M,K = map(int,input().split())
max = 0
while True:
    N-=2
    M-=1
    if N<0 or M<0 or (N+M)< K:
        break
    max+=1
print(max)