from collections import deque

# 이진트리인지 확인하는 함수.


def is_binary(tree):
    q = deque()
    q.append(0)
    visited = [0]*len(tree)
    while q:
        node = q.popleft()
        cnt = 0  # 자식 노드의 개수
        for i in range(len(tree)):
            if tree[node][i] == 1 and not visited[i]:
                visited[i] = 1
                cnt += 1
        if cnt > 2:
            return 0
    return 1

# 이진트리를 생성할 때에는
# tree[i][0]:= i의 왼쪽 자식노드
# tree[i][1]:= i의 오른쪽 자식 노드


# 자신 방문 -> 왼쪽 자식 -> 오른쪽 자식
def preOrder(tree, x):
    if x < 0:
        return
    print(chr(x+ord('A')), end='')

    preOrder(tree, tree[x][0])
    preOrder(tree, tree[x][1])

# 왼쪽 자식 -> 자신 방문 -> 오른쪽 자식


def inOrder(tree, x):
    if x < 0:
        return

    inOrder(tree, tree[x][0])
    print(chr(x+ord('A')), end='')
    inOrder(tree, tree[x][1])

# 왼쪽 자식 ->  오른쪽 자식 -> 자신 방문


def postOrder(tree, x):
    if x < 0:
        return
    postOrder(tree, tree[x][0])
    postOrder(tree, tree[x][1])
    print(chr(x+ord('A')), end='')
