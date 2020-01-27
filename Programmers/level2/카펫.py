'''
[문제 설명]

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 빨간색으로 칠해져 있고 모서리는 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

BBBB
BRRB
BBBB

Leo는 집으로 돌아와서 아까 본 카펫의 빨간색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 빨간색 격자의 수 red가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
빨간색 격자의 수 red는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
입출력 예
brown	red	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]

[문제 풀이]

문제 자체가 설명이 부실하다.

BBBB
BBBB
BRRB
BBBB
BBBB

와 같은 카펫을 고려하는 지에 대한 설명이 없다. 이걸 고려해야한다면 문제가 훨씬 어려워지지만, 이걸 고려하지 않은 것 같다.

따라서 이 문제는 '완전탐색'이 아닌 단순한 '수학' 문제다.
'''


def solution(brown, red):
    total_cnt = brown + red

    for i in range(1, int(total_cnt**0.5)+1):
        if total_cnt % i != 0:
            continue

        row, col = i, total_cnt // i

        if red == (col-2)*(row-2):
            return [col, row]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
