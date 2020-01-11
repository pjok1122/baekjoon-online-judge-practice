'''
[문제 설명]

숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다. 게임해보기

각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
예를 들어, 아래의 경우가 있으면

A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

제한사항
질문의 수는 1 이상 100 이하의 자연수입니다.
baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.
입출력 예
baseball	return
[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	2
입출력 예 설명
문제에 나온 예와 같습니다.

[문제 풀이]

우선 정답이 될 수 있는 키 후보가 최대 [123, 987] 까지 이므로 1000개도 되지 않는다.

따라서 완전탐색으로 정답을 찾아나갈 수 있다.

가장 먼저 정답이 될 수 있는 후보들을 permutation을 이용해서 생성해낸다.

그리고 각 키 후보에 대해서 strike, ball을 계산하여, 후보키인지 아닌지를 확인한다.

만약 후보키가 아니라면(strike,ball이 다르다면), 리스트에서 제거한다.

'''
from itertools import permutations


def solution(baseball):
    answer = [''.join(map(str, tuple_num))
              for tuple_num in permutations(range(1, 10), 3)]

    for num, strike, ball in baseball:
        num = str(num)
        correct = []
        for ans in answer:
            _strike = 0
            _ball = 0
            for j in range(3):
                if ans[j] == num[j]:
                    _strike += 1
                elif ans[j] in num:
                    _ball += 1

            if ans == "124":
                print(_strike, _ball)
            if (_strike, _ball) == (strike, ball):
                correct.append(ans)
        answer = correct

    return len(answer)


solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])
