n = int(input())


def solve(n, x, y):  # 1~n까지의 원판을 x에서 y로 옮기는 함수
    if n == 0:
        return

    solve(n-1, x, 6-x-y)  # 장대 1,2,3 --> x+y+z=6
    print(x, y)
    solve(n-1, 6-x-y, y)


print(2**n-1)
solve(n, 1, 3)
