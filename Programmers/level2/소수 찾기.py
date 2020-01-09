'''
[문제 설명]

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
17	3
011	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.

[문제 풀이]

각 숫자들을 가지고 만들 수 있는 수를 모두 생성합니다.

생성하는 방법은 itertools의 permutations을 사용한 후, set을 이용해 중복되는 값을 필터링 합니다.

생성된 각 수에 대해서 소수판정을 시행합니다.

'''
from itertools import permutations


def solution(numbers):
    permu_num_arr = list(set((map(int, [''.join(j) for i in range(len(numbers))
                                        for j in permutations(numbers, i+1)]))))
    answer = 0

    for num in permu_num_arr:
        if num == 2 or num == 3:
            answer += 1
            continue
        elif num < 2:
            continue

        # 소수 검증
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                break
        else:
            answer += 1
    return answer


'''
에라토스테네스의 체 버전

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
'''

solution("013")
