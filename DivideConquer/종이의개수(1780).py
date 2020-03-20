import sys
input = sys.stdin.readline


def solve(x, y, n):  # (x,y)부터 사이즈가 n인 종이를 사용할 수 있는지 확인하는 함수
    temp = arr[x][y]  # temp는 -1 or 0 or 1
    divide = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != temp:
                divide = 1
                break
    if divide:
        # solve를 나눠서 호출
        m = n//3
        solve(x, y, m)
        solve(x, y+m, m)
        solve(x, y+2*m, m)
        solve(x+m, y, m)
        solve(x+m, y+m, m)
        solve(x+m, y+2*m, m)
        solve(x+2*m, y, m)
        solve(x+2*m, y+m, m)
        solve(x+2*m, y+2*m, m)
    else:
        result[temp+1] += 1


result = [0, 0, 0]  # -1,0,1의 개수를 저장.

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
solve(0, 0, n)

for res in result:
    print(res)
