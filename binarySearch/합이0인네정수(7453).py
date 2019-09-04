'''

'''
from math import ceil
import sys
import bisect as bs

# def binarySearch(target):
#     start = 0
#     end = len(cd)-1
#     mid = (start+end)//2
#     pos = -1
#     while(start<=end):
#         if cd[mid] > target:
#             end = mid-1
#             mid = (start+end)//2
#         elif cd[mid] < target:
#             start = mid+1
#             mid = (start+end)//2
#         else:
#             pos = mid
#             break
    
#     cnt = 0
#     #왼쪽 검사
#     for i in range(pos,-1,-1):
#         if cd[i] == target:
#             cnt+=1
#         else:
#             break

#     #오른쪽 검사
#     for i in range(pos+1,len(cd)):
#         if cd[i] == target:
#             cnt+=1
#         else:
#             break
    
#     return cnt
    
# def binarySearchLower(target):
#     start = 0
#     end = n*n-1
#     mid = (start+end)//2

#     while start<end:
#         if(cd[mid] >= target):
#             end = mid
#             mid = (start+end)//2
#         else:
#             start = mid + 1
#             mid = (start+end)//2

#     if cd[mid] == target:
#         return start
#     else:
#         return -1

# def binarySearchUpper(target,low):
#     start,end =low, n*n-1
#     mid = (start+end)//2
#     while start<end:
#         if cd[mid] <= target:
#             start = mid
#             mid = ceil((start+end)/2)
#         else:
#             end = mid-1
#             mid = (start+end)//2
    
#     if cd[mid] == target:
#         return start
#     else:
#         return -1


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
# for num in ab:
#     low = binarySearchLower(-num)
#     if(low!=-1): #low = -1이면 체크 할 필요 없음.
#         up = binarySearchUpper(-num,0)
#         result += up-low+1
        
# for num in ab:
#     start,end = 0, n*n-1
#     while(start<end):
#         mid = (start+end)//2
#         if cd[mid] >= -num:
#             end = mid
#         else:
#             start = mid+1
    
#     if cd[start] == -num:
#         low = start
#     else:
#         low = -1
    
#     if low == -1:
#         continue

#     start,end = low, n*n-1
#     mid = (start+end)//2
#     while(start<end):
#         if cd[mid] <= -num:
#             start = mid
#             mid = ceil((start+end)/2)
#         else:
#             end = mid-1
#             mid = (start+end)//2
#     if cd[end] == -num:
#         up = start
#     result += up - low + 1

length = len(cd)
for num in ab:
    low = bs.bisect_left(cd,-num)
    if low == length:
        continue
    if cd[low] != -num:
        continue
    else:
        high = bs.bisect_right(cd, -num, low, length-1)
        result += high - low

print(result)