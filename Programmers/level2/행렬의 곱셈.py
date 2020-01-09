'''
[문제 설명]

2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
입출력 예
arr1	arr2	return
[[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]

[문제 풀이]

zip(*A)는 행렬의 Transpose와 동일하다. 따라서 행렬 A,B의 곱셈은 A x zip(*B) 라고 할 수 있다.

'''


def solution2(arr1, arr2):
    return [[sum(a*b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]


def vector_multiple(arr1, arr2, i, j):
    result = 0

    for k in range(len(arr1[0])):
        result += arr1[i][k]*arr2[k][j]

    return result


def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    r = len(arr2[0])

    answer = [[0 for col in range(r)] for row in range(n)]
    for i in range(n):
        for j in range(r):
            answer[i][j] = vector_multiple(arr1, arr2, i, j)

    return answer


print(solution2([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution2([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
                [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
