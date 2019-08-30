'''
이분 탐색을 응용한 문제.
1. Base case와 mid 값을 적절히 조절하는 게 다소 어려운 문제.
'''

from math import ceil

#Itertative
def binarySearch(arr,start,end):
    mid = ceil((start+end)/2)

    while(start<end):
        cnt = 0
        for lan in arr:
            cnt += lan//mid

        #현재 mid가 찾고자 하는 정답일 수도 있기 때문에, start = mid+1이 아니라 start =mid로 둔다.
        #이렇게 설정할 경우 데이터가 두 개 밖에 없을 때, 문제가 발생할 수 있으므로 mid의 값을 ceil로 전진시킨다. 
        if cnt >= N:
            start = mid
            mid = ceil((start+end)/2)
        else:
            end = mid-1
            mid = (start+end)//2
    return start
#Recursive
def FindLAN(data, begin, end, n):
    if begin==end:
        return begin
    count=0
    mid = ceil((begin+end)/2)
    for x in data:
        count+= x//mid
    if count >= n :                  #더 길게 자를 수 있다는 뜻
        return FindLAN(data, mid, end, n)
    else:
        return FindLAN(data, begin, mid-1,n)

K, N = map(int,input().split())
arr = [int(input()) for _ in range(K)]
end = sum(arr)//N

answer = binarySearch(arr, 0,end)
print(answer)