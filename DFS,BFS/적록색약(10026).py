'''
1. BFS, DFS 기본 문제.
2. DFS를 사용할 때에는 sys.setrecursionlimit()을 설정한다.
'''

from collections import deque
import sys
sys.setrecursionlimit(100000)

dx = [0,0,1,-1] 
dy = [1,-1,0,0]

def BFS(sx,sy):
    visited[sx][sy] = 1
    q = deque()
    q.append((sx,sy))
    color = picture[sx][sy]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if(nx<0 or nx>=N or ny<0 or ny>=N):
                continue
            if visited[nx][ny]:
                continue
            if(picture[nx][ny] ==color):
                visited[nx][ny] = 1
                q.append((nx,ny))

# def DFS(sx,sy,color):
#     visited[sx][sy] = 1

#     for i in range(4):
#         nx, ny = sx+dx[i], sy+dy[i]
#         if(nx<0 or nx>=N or ny<0 or ny>=N):
#             continue
#         if visited[nx][ny]:
#             continue
#         if(picture[nx][ny] ==color):
#             DFS(nx,ny,color)


N = int(input())
picture = [list(input()) for _ in range(N)]
visited = [[0 for col in range(N)] for row in range(N)]


# 정상인
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            # DFS(i,j, picture[i][j])
            cnt+=1

print(cnt, end= ' ')

# 적록색약
for i in range(N):
    for j in range(N):
        if picture[i][j] =='G':
            picture[i][j] = 'R'
cnt=0
visited = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            # DFS(i,j, picture[i][j])
            cnt+=1
print(cnt)