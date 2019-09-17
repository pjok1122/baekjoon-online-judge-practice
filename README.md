## Greedy Algorithm

 현재 상황에서 가장 최적인 방법을 선택하여 문제를 해결하는 기법.

 백준에서 직접 문제를 선별하였습니다.

 1. 입력이 빈번하게 일어나는 경우, input() 대신, sys.stdin.readline()을 사용하는 것이 좋습니다.

## [N and M](https://github.com/pjok1122/backjoon-algorithm-practice/tree/master/N_and_M)

 재귀함수와 백트래킹을 공부할 수 있는 가장 좋은 문제집입니다.

 라이브러리를 사용하여 구현할 수 있지만 직접 구현해보는 것이 좋습니다.

 Python 참고 라이브러리 : itertools

 모듈 : permutations, combinations 

## DFS BFS

 알고리즘 대회에서 가장 많이 출제되는 유형입니다.

 깊이우선 탐색(DFS)은 Stack을 이용하여 모든 노드를 탐색하는 기법이며,

 너비우선탐색(BFS)은 Queue를 이용하여 모든 노드를 탐색하는 기법입니다.

1. Queue를 구현할 때 queue 라이브러리를 사용할 경우 Thread safe하다는 장점은 있지만, 단일 쓰레드의 경우에는 속도가 현저하게 느려집니다. 따라서 collections 라이브러리에 존재하는 deque를 사용하는 것이 좋습니다.
   - popleft(), append() 연산 사용 가능.

2. BFS와 DFS는 visited 라는 배열을 이용해, 방문여부를 파악합니다.

3. BFS의 경우, Queue에 node 번호 외에 value를 추가로 전달하여 구현하기도 합니다.

4. 현재 노드로부터 이동할 수 있는 위치가 다양할 경우, dx[], dy[] 라는 리스트를 만들어 해결합니다.

##  Dynamic Programming

 DP는 이미 계산된 결과를 다시 계산하지 않도록, 메모리에 값을 저장해두는 프로그래밍 기법입니다.

 Bottom-up(Iterative), Top-down(Recursive) 방식이 존재하지만, 두 방식 중 하나라도 잘 구현할 수 있으면 됩니다.

 1. DP의 핵심은 배열이 갖는 의미를 명확히 정의하는 것입니다.
 
 ex) dp[n] := n이 숫자 1이 될 때까지 필요한 연산의 최소 횟수

 2. DP 자체만으로 문제를 출제하는 경우는 많지 않습니다. BFS와 연계된 문제에 집중하세요.

## Binary Search

 이진탐색은 정렬된 데이터에 대해서 log(N) 복잡도를 가지는 탐색 기법입니다.

 단순히 원하는 값을 찾으면 멈추는 알고리즘도 있지만, 최대 인덱스나 최소 인덱스를 찾는 요령을 익혀두는 것이 좋습니다.