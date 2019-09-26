'''
[문제 풀기 전 생각할 것]

각 노드의 부모 노드를 구하는 문제이지만, 입력으로 주어지는 데이터는 간선(edge)에 대한 정보다.

따라서 주어진 간선 정보를 '인접 행렬' 이나 '인접 리스트' 형태로 저장해야 한다.

대부분의 경우 '인접 행렬'은 데이터의 낭비가 심하고 복잡도가 높으므로 '인접 리스트'로 데이터를 저장한다.

만약 간선의 정보가 다음과 같이 주어졌다고 해보자.

간선 : [[1,2], [1,3], [2,5],[5,4]]

그림으로 나타내면,

        1
    2       3
    5
    4

형태로 이어진 트리라고 할 수 있다.

1. 1과 연결된 2,3은 부모 노드가 1임을 알 수 있다. 또 각 노드 2번 3번과 연결된 노드를 탐색한다.
2. 2번 노드는 1번 노드와 5번 노드와 연결되어있다. 1번 노드는 이미 방문을 했으니 제외하고, 5번 노드를 방문한다.
3. 5번 노드의 부모 노드는 2번으로 설정한다.

즉, BFS를 이용해 문제를 풀어나갈 수 있다.

'''
def BFS(s):
    q = deque()
    q.append(s)

    while q:
        s = q.popleft()
        for v in edge[s]:
            if not visited[v]:
                visited[v]=1
                parent[v] = s
                q.append(v)


import sys
from collections import deque

n = int(input())
edge=[[] for i in range(n+1)]
visited=[0]*(n+1)
parent=[0]*(n+1)
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

BFS(1)

for p in parent[2:]:
    print(p)
