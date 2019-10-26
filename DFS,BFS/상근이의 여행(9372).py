'''

[문제 풀기 전 생각할 것]


이 문제는 BFS/DFS로 분류되지만, 잘못 출제된 문제에 가깝다.


주어진 문제 조건을 보면, 모든 국가는 연결그래프이다. 연결 그래프라는 것은 모든 국가가 이어져있어서, 비행기로 갈 수 없는 국가가 없다는 뜻이다.


그럼 N개의 국가를 여행할 때 몇 종류의 비행기를 타야할까? 직접 여행은 간다고 생각해보자.


대만, 일본, 태국을 방문하려고 한다면, 다음 두 편도 비행기를 타면 된다. (출발지를 맘대로 설정할 수 있기 때문)


대만 -> 일본

일본 -> 태국


따라서 모든 경우에 정답이 N-1이 됨을 알 수 있다.

'''

import sys
T = int(input())

for test_case in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    print(N-1)
