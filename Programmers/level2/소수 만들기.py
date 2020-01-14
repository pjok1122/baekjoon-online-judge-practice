'''
[문제 설명]

주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
입출력 예
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
입출력 예 설명
입출력 예 #1
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.

[문제 풀이]

쉬운 문제. combinations을 적용하고 각 수에 대해서 소수판정 알고리즘을 시행.

소수 판정 알고리즘은 1) sqrt(n)까지 나눠 보는 방식, 2) 에라토스 테네스의 체

선택으로 풀 수 있다.


'''


from itertools import combinations


def solution(nums):
    nums = list(combinations(nums, 3))
    answer = 0
    for num in nums:
        sum_num = sum(num)

        #sum_num >=6
        for i in range(2, int(sum_num**(0.5))+1):
            if sum_num % i == 0:
                break
        else:
            answer += 1

    return answer
