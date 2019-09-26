'''
[문제 풀기 전 생각할 것]

가장 먼저 데이터를 어떻게 저장할 것 인지에 대해서 생각해봐야 한다.

주어진 문자는 'A'부터 'Z'까지 이므로 0에서 25의 숫자로 대응이 가능하다.

또한, 순회를 하는 것이 목적이기 때문에, 자식 노드의 번호를 저장해두는 방법을 선택한다.

위 작업을 요약하면, 다음과 같다.

트리의 각 노드를 0~25로 지정하고, 노드 i의 자식 노드를 a[i][0], a[i][1]에 저장한다.


[알고리즘]

입력 : [[A B C] [B D .] ....]

1. 주어진 입력 [A,B,C]를 a[0][0] = 1, a[0][1] = 2 형태로 바꾸어 저장한다.
2. 각 노드에 대해서 전위순회, 중위순회, 후위순회 알고리즘을 적용하면 된다.
'''
import sys

# 자신 방문 -> 왼쪽 자식 -> 오른쪽 자식
def preOrder(x):
    if x<0:
        return
    print(chr(x+ord('A')), end='')

    preOrder(tree[x][0])
    preOrder(tree[x][1])

# 왼쪽 자식 -> 자신 방문 -> 오른쪽 자식
def inOrder(x):
    if x<0:
        return

    inOrder(tree[x][0])
    print(chr(x+ord('A')), end='')
    inOrder(tree[x][1])

# 왼쪽 자식 ->  오른쪽 자식 -> 자신 방문 
def postOrder(x):
    if x<0:
        return
    postOrder(tree[x][0])
    postOrder(tree[x][1])
    print(chr(x+ord('A')), end='')

n = int(input())
tree=[[-1 for col in range(2)] for row in range(n)]
for i in range(n):
    p,c1,c2 = map(lambda x:ord(x)-ord('A'), sys.stdin.readline().split())
    
    if 0<=c1<=25:
        tree[p][0] = c1
    if 0<=c2<=25:
        tree[p][1] = c2

preOrder(0)
print()
inOrder(0)
print()
postOrder(0)

