'''
1. 전수조사를 진행한다면 시간복잡도는 10! 이라는 것을 알 수 있음. (순열로 풀 수 있음.)
2. 하지만, 부등호가 만족되지 않는다면 더 이상 깊이 탐색할 필요가 없음. (Branch and bound나 backtracking을 떠올리는 것이 일반적)
3. 최댓값과 최솟값을 찾으면 되기 때문에 함수를 분할하는 것이 타당.
'''

# def findPath(depth,result):
#     if depth==k+1:
#         print(result)
#         return
#     for i in range(9,-1,-1):
#         result[depth] = i
#         if depth==0:
#             visited[i] = 1
#             findPath(depth+1, result)
#             visited[i] = 0
#         else:
#             if visited[i]: #방문했는가?
#                 continue
#             elif ineq[depth-1] == '<' and result[depth-1] > result[depth]: #잘못된 Path인가?
#                 continue
#             elif ineq[depth-1] == '>' and result[depth-1] < result[depth]: #잘못된 Path 인가?
#                 continue
#             else:
#                 visited[i] = 1
#                 findPath(depth+1, result)
#                 visited[i] = 0

def findPathMax(depth,result):
    global find
    if depth==k+1:
        find = 1
        return
    for i in range(9,-1,-1):
        if find:
            return
        result[depth] = i

        if depth==0:
            visited[i] = 1
            findPathMax(depth+1, result)
            visited[i] = 0
        else:
            if visited[i]: #방문했는가?
                continue
            elif ineq[depth-1] == '<' and result[depth-1] > result[depth]: #잘못된 Path인가?
                break
            elif ineq[depth-1] == '>' and result[depth-1] < result[depth]: #잘못된 Path 인가?
                continue
            else:
                visited[i] = 1
                findPathMax(depth+1, result)
                visited[i] = 0

def findPathMin(depth,result):
    global find
    if depth==k+1:
        find = 1
        return
    for i in range(0,10):
        if find:
            return
        result[depth] = i
        
        if depth==0:
            visited[i] = 1
            findPathMin(depth+1, result)
            visited[i] = 0
        else:
            if visited[i]: #방문했는가?
                continue
            elif ineq[depth-1] == '<' and result[depth-1] > result[depth]: #잘못된 Path인가?
                continue
            elif ineq[depth-1] == '>' and result[depth-1] < result[depth]: #잘못된 Path 인가?
                break
            else:
                visited[i] = 1
                findPathMin(depth+1, result)
                visited[i] = 0


k = int(input())
ineq = input().split()
result =[-1]*(k+1)
visited = [0]*(10)
find = 0
findPathMax(0, result)
print(''.join(str(e) for e in result))
find = 0
findPathMin(0, result)
print(''.join(str(e) for e in result))