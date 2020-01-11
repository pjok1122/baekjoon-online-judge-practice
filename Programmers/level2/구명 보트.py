'''
[문제 설명]

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
입출력 예
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3

[문제 풀이]

쉬운 문제. 사람들의 몸무게를 오름차순으로 정렬한 후, 가장 무거운 사람을 뽑는다.

가장 무거운 사람의 몸무게에 가장 가벼운 사람의 몸무게를 더할 수 있을 때까지 더해 나간다.

사람이 전부 구출될 때까지 반복하면 끝.

pop연산을 호출하다보면 시간 초과가 발생하는데, pop(0)은 Shift 연산 오버헤드 때문에 O(n) 이기 때문이다.

따라서 인덱스를 조절해서 풀거나, deque를 이용해 양방향에서 데이터를 뽑는다면 문제 없이 해결이 가능하다.

deque은 양방향 삽입,삭제의 시간복잡도가 O(1)이기 때문이다.
'''

# pop 연산으로 인한 리스트 Shift 연산이 시간초과의 원인이 되는 것 같음.
'''
def solution(people, limit):
    people.sort()
    answer = 0
    while len(people):
        heavy = people.pop(-1)
        while len(people) > 0 and heavy + people[0] <= limit:
            heavy += people.pop(0)
        answer += 1
    print(answer)
    return answer
'''


def solution(people, limit):
    people.sort()
    answer = 0
    left, right = 0, len(people)-1
    while left <= right:
        heavy = people[right]
        for i in range(left, right):
            if heavy + people[i] <= limit:
                heavy += people[i]
                left += 1
            else:
                break
        right -= 1
        answer += 1
    print(answer)
    return answer


solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)
