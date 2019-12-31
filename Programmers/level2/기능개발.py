'''
[문제]

프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

입출력 예
progresses	speeds	return
[93,30,55]	[1,30,5]	[2,1]
입출력 예 설명
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

[문제 풀이]

각 작업(progreess)이 끝나는 데에 며칠이 걸리는 지만 계산해 놓으면 손쉽게 파악할 수 있다. 작업을 끝내는 데 걸리는 시간(completion_date)이 [7,3,9] 라고 해보자.

첫 작업이 7일에 걸쳐 완성되므로, 그 이후의 인덱스에서 7보다 작은 값이 존재할 때마다 카운트를 1씩 증가시킨다.
만약 7보다 큰 값이 존재하면, 이전에 계산한 카운트를 result에 삽입하고, 카운트를 다시 1로 셋팅한다. 그리고 위의 과정을 반복한다.

'''
import math


def solution(progresses, speeds):
    completion_date = []
    answer = []
    completion_date = [math.ceil((100-progress)/speeds[i])
                       for i, progress in enumerate(progresses)]

    now = completion_date.pop(0)
    count = 1
    for date in completion_date:
        if date <= now:
            count += 1
            continue

        if date > now:
            answer.append(count)
            now = date
            count = 1

    answer.append(count)

    return answer


solution([93, 30, 55], [1, 30, 5])
