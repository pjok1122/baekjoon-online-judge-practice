'''
순열에서 k번째 순열 찾기.

Bactracking으로 찾는 문제가 아니고, k번째를 그리디하게 찾아 나가는 알고리즘.


'''

import math

count = 0
is_answer = False

def solution2(n,k):
    people = list(range(1,n+1))
    result = []
    people_cnt = n
    while len(result) < people_cnt:
        factorial = math.factorial(n-1)
        q, k = (k-1)//factorial, k%(factorial)
        n = n-1

        result.append(people.pop(q))

    return result

def solution(n, k):
    result = [-1]*n    
    visited = [0]*n

    num = math.factorial(n-1)
    q, k = k//num,k%num
    visited[q] = 1
    result[0] = q
    dfs(1, n, k, visited, result)

    return list(map(lambda x:x+1, result))


def dfs(depth, n, k, visited, result):
    global count
    global is_answer

    if is_answer:
        return

    if depth == n:
        count+=1

    if count >= k:
        is_answer = True
        return

    if depth < n:
        for i in range(n):
            if is_answer:
                return
            
            if not visited[i]:
                visited[i] = 1
                result[depth] = i
                dfs(depth+1, n, k, visited, result)
                visited[i] = 0


print(solution2(4, 20))
print(solution(4, 20))