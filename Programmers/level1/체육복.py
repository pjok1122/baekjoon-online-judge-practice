import bisect


def solution(n, lost, reserve):
    answer = n-len(lost)

    for i, target in enumerate(lost):
        if target in reserve:
            answer += 1
            lost[i] = 0
            reserve.remove(target)

    lost.sort()
    reserve.sort()

    for target in lost:
        if target <= 0:
            continue
        index = bisect.bisect_left(reserve, target)
        if index > 0 and target-1 == reserve[index-1]:
            answer += 1
            del(reserve[index-1])
        elif index < len(reserve) and target+1 == reserve[index]:
            answer += 1
            del(reserve[index])

    return answer


# print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2, 4], [3]))
# print(solution(5, [1], [1]))
print(solution(3, [1, 2, 3], [1, 2, 3]))
print(solution(5, [1, 2, 3, 4], [2, 4, 5]))
