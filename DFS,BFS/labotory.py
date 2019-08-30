'''
* 배운 점
1. 깊은 복사를 사용할 경우 : 메모리 사용량이 매우 크며, 많은 시간이 소요됨.
2. combinations을 사용한 결과를 변수에 담지 않고 for문에 바로 적용하는 것이 좋음.
3. 주어진 시간과 N,M의 사이즈를 고려하여 완전탐색을 시도할지 결정한다.

'''


from itertools import combinations as cb
from collections import deque
import copy

dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt0=0
cnt2=0
Min =10000
def BFS(sx, sy):
    global cnt2
    q = deque()
    q.append((sx,sy))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if(nx<0 or nx>=N):
                continue
            if(ny<0 or ny>=M):
                continue
            if not Map[nx][ny]:   #벽도 아니고 바이러스도 아니라면,
                Map[nx][ny] = 3
                cnt2+=1
                q.append((nx,ny))
cand =[]
virus=[]
N,M = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not Map[i][j]: #Map[i][j] ==0 이면,
            cand.append((i,j))
            cnt0+=1
        elif Map[i][j]==2:
            virus.append((i,j))


for wall in list(cb(cand,3)): #wall = [(x1,y1),(x2,y2),(x3,y3)]
    # Tmp = copy.deepcopy(Map) #깊은 복사의 속도가 아주 느리다는 것을 알 수 있음.
    cnt2 = 0
    for w in wall:
        Map[w[0]][w[1]] = 1
    for v in virus:
        BFS(v[0],v[1])
    
    if(Min > cnt2):
        Min = cnt2

    for w in wall:
        Map[w[0]][w[1]] = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 3:
                Map[i][j] = 0

print(cnt0-Min-3)
