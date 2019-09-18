'''
[문제]
3x3 부분행렬의 값을 전부 0->1 ,1->0으로 뒤집을 수 있는 연산을 가지고,
A행렬 -> B행렬로 만드는 최소 연산 횟수를 구하여라.

[문제 풀기 전 생각할 것]

(0,0) (N-1,0), (0, M-1), (N-1,M-1)의 값을 결정할 수 있는 부분행렬은 딱 1개밖에 존재하지 않는다.

즉, (0,0)에서 3x3 매트릭스를 그려서, A[0][0] != B[0][0] 이라면 3x3 매트릭스에 해당하는 값을 전부 뒤집는다.

이제, (0,1)에 영향을 주는 매트릭스는 (0,1)을 꼭지점으로 하는 매트릭스 하나뿐이다. 마찬가지로 A[0][1] != B[0][1]을 확인한다.

위의 예시처럼 → 방향으로 순서대로 확인을 해나간다.

[알고리즘]

1. 3x3매트릭스의 특성을 고려하면 x의 범위는 [0,N-2] 이고 y의 범위는 [0, M-2]이다.
2. [i][j]를 하나씩 늘려가며, flip(x,y)연산을 호출한다.
3. 마지막에는 A행렬과 B행렬이 같은지를 확인하고 같다면 flip 호출 횟수를, 다르다면 -1을 반환한다.

'''

N, M =map(int,input().split())

A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

def flip(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j] = 1 - A[i][j]

def checkEquality():
    for i in range(N):
        for j in range(M):
            if A[i][j] !=B[i][j]:
                return 0
    return 1

cnt = 0
for i in range(0,N-2):
    for j in range(0,M-2):
        if A[i][j] !=B[i][j]:
            flip(i,j)
            cnt+=1

if checkEquality():
    print(cnt)
else:
    print(-1)