'''
    1. 모든 사람의 ATM 대기시간의 합이 최소가 되도록 설정하는 문제.
    2. 업무 시간이 가장 짧은 사람을 먼저 할당하는 것이 핵심 아이디어. 해당 사람이 업무를 보는 동안 모든 사람들의 대기시간이 누적되기 때문.
    3. 따라서 대기시간을 오름차순으로 정렬한다. O(nlogn)
    4. 오름차순으로 정렬된 시간대로 대기시간을 누적시키면 된다. O(n)
    5. 시간복잡도 O(nlogn + n) = O(nlogn)
'''

n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0
for i in range(n):
    result += time[i]*(n-i)

print(result)
