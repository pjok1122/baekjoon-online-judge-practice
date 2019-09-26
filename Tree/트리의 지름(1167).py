'''
[문제 풀기 전 생각할 것]

트리의 지름이란, 가장 길이가 긴 경로를 찾으란 말과 동치다.

임의의 노드에서 출발하면 모든 노드까지의 거리를 잴 수 있다.

하지만, 임의의 노드에서 출발했을 때 얻어진 가장 긴 거리가 항상 트리의 지름이 될까?

그렇지 않다. '스타' 형태로 연결된 트리를 생각해보자. '스타'의 중앙에서 출발한다면, 모든 노드까지의 거리가 1이다.

하지만 1은 트리의 지름이 아니다. 왜냐하면 스타의 꼭지점에서 출발하여 반대쪽 꼭지점까지의 거리는 2가 되기 때문이다.

가장 쉬운 방법은 모든 노드에서 출발해서 거리를 재보고, 그 때의 Max값을 최종 결과로 제출하면 된다.

이것도 틀린 방법은 아니지만, 더 좋은 방법이 있다.

[알고리즘]

1. 임의의 노드에서 출발하여 가장 거리가 먼 노드와 경로를 찾는다. (BFS 1회)
2. 그 노드를 시작점으로 하여 가장 거리가 먼 노드와 경로를 찾는다. (BFS 2회)
3. 앞서 1과 2에서 계산된 경로 중 길이가 더 긴 경로가 정답이 된다.

'''
import sys
from collections import deque

def BFS(s):
    q = deque()
    dist = 0 #가장 먼 거리
    dest = 0 #가장 먼 노드
    visited[s] = 1
    q.append((s,0))
    while q:
        s,c = q.popleft()
        for v,nc in edge[s]:
            if not visited[v]:
                visited[v] = 1
                q.append((v,c+nc))
                if c+nc >= dist:
                    dist = c+nc
                    dest = v
    return [dest, dist]

v = int(sys.stdin.readline())
edge=[[] for _ in range(v+1)]
visited=[0]*(v+1)
for _ in range(v):
    info = list(map(int,sys.stdin.readline().split()))
    s = info[0]
    for i in range(1, len(info)-1, 2):
        edge[s].append((info[i], info[i+1]))

start, Max = BFS(1)

# visited 초기화
for i in range(v+1):
    visited[i] = 0

dest, dist = BFS(start)

if Max > dist:
    print(Max)
else:
    print(dist)

