# Greedy Algorithm

 현재 상황에서 가장 최적인 방법을 선택하여 문제를 해결하는 기법.

 백준에서 직접 문제를 선별하였습니다.

 입력이 빈번하게 일어나는 경우,

 input() 대신, sys.stdin.readline()을 사용하는 것이 좋습니다.

# N and M

 재귀함수와 백트래킹을 공부할 수 있는 가장 좋은 문제집입니다.

 라이브러리를 사용하여 구현할 수 있지만 직접 구현해보는 것이 좋습니다.

 Python 참고 라이브러리 : itertools

 모듈 : permutations, combinations 

# DFS BFS

알고리즘 대회에서 가장 많이 출제되는 유형입니다.

깊이우선 탐색(DFS)은 Stack을 이용하여 모든 노드를 탐색하는 기법이며,

너비우선탐색(BFS)은 Queue를 이용하여 모든 노드를 탐색하는 기법입니다.

Queue를 구현할 때 queue 라이브러리를 사용할 경우 Thread safe하다는 장점은 있지만, 단일 쓰레드의 경우에는 속도가 현저하게 느려집니다.

따라서 collections 라이브러리에 존재하는 deque를 사용하는 것이 좋습니다.

popleft(), append() 연산 사용 가능.