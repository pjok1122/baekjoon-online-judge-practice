import sys
from collections import deque
n, m = map(int, input().split())
# arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
arr = [sys.stdin.readline() for _ in range(n)]
visited = [[0 for col in range(m)] for row in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(sx, sy):
    q = deque()
    visited[sx][sy] = 1
    q.append((sx, sy, 1))
    while q:
        x, y, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '1'and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, cnt+1))


print(bfs(0, 0))
