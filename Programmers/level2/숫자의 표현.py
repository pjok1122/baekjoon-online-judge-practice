'''
[문제 설명]

Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
입출력 예
n	result
15	4
입출력 예 설명
입출력 예#1
문제의 예시와 같습니다.

[문제 풀이]

등차수열을 이용해서 등식이 성립할 수 있는 a1과 몇개를 더해야 하는지를 파악하는 방법도 있다.

하지만, 숫자의 크기가 10000밖에 안되므로 완전탐색으로 풀어도 충분하다.
'''


def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum_of_num = 0
        for j in range(i, n+1):
            sum_of_num += j
            if sum_of_num == n:
                answer += 1
            elif sum_of_num > n:
                break

    return answer


print(solution(15))
