'''
1. A+B가 될 수 있는 값을 모두 저장한 배열 AB,
2. C+D가 될 수 있는 값을 모두 저장한 배열 CD로 나눈다.
3. CD를 오름차순으로 정렬하고, AB의 각 원소마다 Binary Search를 시작한다.
4. 만약 값이 존재하지 않으면 더이상 탐색하지 않고, 값이 존재한다면 그 중에서 가장 왼쪽 인덱스를 찾는다.
5. 왼쪽 인덱스로부터 탐색을 시작하여, 가장 오른쪽 인덱스를 찾는 Binary Search를 한번 더 수행한다.
'''
from math import ceil
import sys

n = int(sys.stdin.readline())
arr =[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ab=[]
cd=[]
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

cd.sort()
low,up =0,0
result = 0

for num in ab:
    start,end = 0, n*n-1
    while(start<end):
        mid = (start+end)//2
        if cd[mid] >= -num:
            end = mid
        else:
            start = mid+1
    
    if cd[start] == -num:
        low = start
    else:
        low = -1
    
    if low == -1:
        continue

    start,end = low, n*n-1
    mid = (start+end)//2
    while(start<end):
        if cd[mid] <= -num:
            start = mid
            mid = ceil((start+end)/2)
        else:
            end = mid-1
            mid = (start+end)//2
    if cd[end] == -num:
        up = start
    result += up - low + 1

print(result)