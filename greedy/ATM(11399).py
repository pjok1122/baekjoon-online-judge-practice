'''
모든 사람의 ATM 대기시간의 합이 최소가 되도록 설정하는 문제.
   
[문제 풀기 전 생각할 것]

업무 시간이 짧은 사람 먼저 업무를 보는 것이, 대기시간의 총합은 가장 적다.
해당 사람이 업무를 보는 동안 모든 사람들의 대기시간이 누적되기 때문.
따라서 대기시간을 오름차순으로 정렬한다. O(nlogn)

오름차순으로 정렬된 시간대로 대기시간을 누적시키면 된다. O(n)
시간복잡도 O(nlogn + n) = O(nlogn)
'''

n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0
for i in range(n):
    result += time[i]*(n-i)

print(result)
