def solution(n, lost, reserve):
    answer = n-len(lost)
    lost.sort()
    reserve.sort()

    for target in lost:
        if target in reserve:
            reserve.remove(target)
            answer += 1
            continue

        for cloth in reserve:
            if cloth == target-1 or cloth == target+1:
                reserve.remove(cloth)
                answer += 1
                break

    return answer


print(solution(5, [1, 2, 3, 4], [2, 4, 5]))
