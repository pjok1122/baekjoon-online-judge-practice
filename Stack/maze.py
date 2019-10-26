'''
미로 찾기

4 6
1 0 1 1 1 0
1 0 1 0 1 1
1 0 1 0 1 0
1 1 1 0 1 1

4 4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 0

'''

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for col in range(m)] for row in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 스택으로 구현한다면, 돌아올 곳을 stack에 push한다는 느낌으로 작성.


def find_path(x, y, ex, ey):
    stack = []
    stack.append((x, y))
    while len(stack):
        if (x, y) == (ex, ey):
            return 1
        elif x-1 >= 0 and arr[x-1][y] == 1 and not visited[x-1][y]:
            stack.append((x, y))
            x = x-1
            visited[x][y] = 1
        elif x+1 < n and arr[x+1][y] == 1 and not visited[x+1][y]:
            stack.append((x, y))
            x = x+1
            visited[x][y] = 1
        elif y-1 >= 0 and arr[x][y-1] == 1 and not visited[x][y-1]:
            stack.append((x, y))
            y = y-1
            visited[x][y] = 1
        elif y+1 < m and arr[x][y+1] == 1 and not visited[x][y+1]:
            stack.append((x, y))
            y = y+1
            visited[x][y] = 1
        else:
            x, y = stack.pop(-1)

    return 0


print(find_path(0, 0, n-1, m-1))
