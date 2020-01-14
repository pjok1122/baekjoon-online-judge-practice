'''
[문제 설명]
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3
입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.

[문제 풀이]

이해하기가 약간 까다로운 문제이나, 쉬운 문제.

H-index는 결국, "h 인용된 논문이 h개 이상있느냐" 로 결정된다.

h라는 기준을 어떻게 잡을 지 결정하는 것이 이 문제의 Key Point이다.

최댓값이니 분명 큰 수부터 내려가는 것이 바람직하다. 하지만 어떤 값부터 출발해야할까?

우리의 기준은 citations의 최댓값과 len(citations) 중에 결정해야 한다.  (각각의 예시를 만들어보고 생각해보자.)

citations이 아무리 커도, len(citations)을 넘어서는 순간 h-index를 만족할 수 없다.

따라서 우리는 len(citations)을 기준으로 하는 것이 훨씬 간단하다는 것을 짐작할 수 있다.

따라서 len(citations)을 값을 하나씩 줄여나가며 체크하면 된다.

h-index가 len(citations)가 되려면, 모든 citation 값이 len(citations)보다 커야한다.

따라서 citations을 정렬해두고, 가장 작은 값이 len(citations)보다 큰 지 비교하면 된다.


'''


def solution(citations):
    citations.sort()
    answer = 0
    for i, j in zip(range(len(citations), -1, -1), range(len(citations))):
        if citations[j] >= i:
            answer = i
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
print(solution([22, 42]))
print(solution([0, 0, 0]))
print(solution([20, 19, 18, 1]))
