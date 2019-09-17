## DFS BFS

 알고리즘 대회에서 가장 많이 출제되는 유형입니다.

 깊이우선 탐색(DFS)은 Stack을 이용하여 모든 노드를 탐색하는 기법이며,

 너비우선탐색(BFS)은 Queue를 이용하여 모든 노드를 탐색하는 기법입니다.

1. Queue를 구현할 때 queue 라이브러리를 사용할 경우 Thread safe하다는 장점은 있지만, 단일 쓰레드의 경우에는 속도가 현저하게 느려집니다.

따라서 collections 라이브러리에 존재하는 deque를 사용하는 것이 좋습니다.

   ex) popleft(), append() 연산 사용 가능.

2. BFS와 DFS는 visited 라는 배열을 이용해, 방문여부를 파악합니다.

3. BFS의 경우, Queue에 node 번호 외에 value를 추가로 전달하여 구현하기도 합니다.

4. 현재 노드로부터 이동할 수 있는 위치가 다양할 경우, dx[], dy[] 라는 리스트를 만들어 해결합니다.

## 소스 코드 

```python
# DFS : O(n+m)
def DFS(start): 
    visited[start] = 1
    for i in edge[start]:
        if not visited[i]: 
            DFS(i)
```


```python
# BFS : O(n+m)
#from queue import Queue
from collections import deque
def BFS(start):
    que = deque()
    visited[start] = 1
    while que:
        v = que.popleft()
        for i in edge[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = 1
```

1. Queue에 (node, value) 형태로 데이터를 삽입하는 요령을 익혀두면 좋습니다.

2. 1차원 노드가 아니고, 연결된 엣지가 방향이 존재한다면 dx[], dy[]라는 방향 리스트를 만드는 것이 좋습니다.

```python
dx=[-1,-2,-2,-1,1,2,1,2]
dy=[-2,-1,1,2,-2,-1,2,1]

def BFS(x,y):
    que = deque()
    visited[x][y] = 1
    que.append((x,y,step))
    while que:
        x,y = que.popleft()
        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]
            if (nx<0 or ny<0 or nx>=L or ny>=L):
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                que.append((nx,ny))
```