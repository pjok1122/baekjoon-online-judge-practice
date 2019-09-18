import sys
sys.setrecursionlimit(10**6)

#재귀함수를 이용한 풀이
def binarySearch_R(arr, target, s,e):
    m = (s+e)//2

    #베이스 케이스
    if arr[m] == target:
        return 1
    elif s>=e:
        return 0
    elif arr[m] < target:
        return binarySearch_R(arr,target,m+1,e)
    elif arr[m] > target:
        return binarySearch_R(arr,target,s,m-1)
    

# Iterative
def binarySearch(arr, target):
    s = 0
    e = len(arr) - 1
    m = (s+e)//2
    while (s<=e):
        if arr[m] == target:
            return 1
        elif arr[m] < target:
            s = m + 1
            m = (s+e)//2
        elif arr[m] > target:
            e = m - 1
            m = (s+e)//2
    return 0

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))
arr.sort()

for t in target:
    # print(binarySearch(arr,t))
    print(binarySearch_R(arr,t,0, N-1))
