'''
문제 : N개의 로프가 주어지는데, 로프가 견딜 수 있는 무게는 각각 다르다. 로프를 K개 사용하면 각 로프가 받는 무게는 W/K로 정확하게 나눠진다.
       로프를 적절히 배합하여 견딜 수 있는 최대 무게를 찾아라.

1. 로프의 개수가 100000개까지 나올 수 있으므로 상대적으로 입출력이 빠른 sys.stdin.readline()을 사용한다.
2. 로프를 K개 선택했다고 했을 때, 해당 로프 조합이 견딜 수 있는 최대 무게는, 가장 약한 로프에 의존한다.
3. 따라서 로프를 오름차순으로 정렬하여 사용하는 것이 바람직하다.
4. 로프를 오름차순으로 정렬한 후, N개의 로프를 선택했을 때부터 1개의 로프를 선택했을 때까지 모든 무게를 계산하여 결과를 도출한다.
5. 시간복잡도 : O(nlogn) + O(n)
'''
import sys

N = int(input())
rope =[]
# rope =[0]*N
for i in range(N):
    rope.append(int(sys.stdin.readline()))
    # rope[i] = int(sys.stdin.readline())

rope.sort() #nlogn
Max = 0
for i in range(N):
    tmp = (N-i)*rope[i]
    if Max < tmp:
        Max = tmp

print(Max)