'''
[문제]

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
JEROEN	56
JAN	23

[문제 풀이]

문제에서는 Optimal한 Solution을 찾으라는 늬앙스이지만, 실제로는 Greedy한 알고리즘을 짜는게 문제다. 즉, 우리의 알고리즘은 최적의 알고리즘이 될 수 없다.

단순히 Greedy하게 현재 커서 위치에서 왼쪽으로 이동하느냐, 오른쪽으로 이동하느냐를 결정해야 한다. 왼쪽에 'A'가 아닌 문자가 가까이 있는지 오른쪽에 'A'가 아닌 문자가 가까이 있는지를
계산하여 가까운 곳을 선택하면 된다.

커서가 위아래로 움직이는 연산은 'A'~'Z'가 26가지의 문자가 존재하므로 시간복잡도 1로 계산이 가능하다.


'''


def solution(name):
    name = list(name)
    result = 0
    indexes = []
    length = len(name)
    for i, v in enumerate(name):
        if v != 'A':
            result += min(ord(v)-ord('A'),
                          26-ord(v)+ord('A'))
            indexes.append(i)

    cur_index = 0
    while(len(indexes)):
        right = indexes[0] - cur_index if indexes[0] - \
            cur_index >= 0 else length + indexes[0] - cur_index
        left = cur_index - indexes[-1] if cur_index - \
            indexes[-1] >= 0 else length + cur_index - indexes[-1]

        if right <= left:
            result += right
            cur_index = indexes.pop(0)
        else:
            result += left
            cur_index = indexes.pop(-1)

    return result


print(solution("BBAABAAAB"))  # 답은 9여야함.
