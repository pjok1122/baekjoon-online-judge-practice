'''
[문제 풀기에 앞서 생각할 것]

1. 랜선의 길이를 찾는 문제이기 때문에, '랜선의 길이'를 Binary Search로 찾아나간다.
2. '랜선의 길이'가 길어질 수록 랜선의 개수 (K)는 적어진다. 반대로 '랜선의 길이'가 짧아질 수록 랜선의 개수 (K)는 많아진다.

[B.S 알고리즘]

문제의 예시처럼,
목표 랜선의 개수 : 11개
랜선 : [457, 539, 743, 802] 가 주어졌다고 하자.

'랜선의 길이'는 1부터 (457+539+743+802)/11 까지 가질 수 있지만, 편의상 802로 놓아도 문제 없다.

따라서 1~802 사이에 정답이 존재한다.

B.S를 적용하여 '랜선의 길이' mid = (1+802)/2 --> 401로 설정하자.

이 때 랜선의 개수가 몇개가 나오는지 계산하는 알고리즘이 필요하다.

[랜선의 개수 알고리즘]

예시 [457, 539, 743, 802], 랜선 길이 : 401

1. 457에서는 1개의 랜선이 나온다.
2. 539에서는 1개의 랜선이 나온다.
3. 743에서는 1개의 랜선이 나온다.
4. 802에서는 2개의 랜선이 나온다.
5. 랜선의 개수의 총합인 5를 반환한다.
----------------------------------------------------------------------------------

mid = 401 일 때, 랜선의 개수가 5이므로 랜선을 더 짧게 잘라야 한다. 따라서 mid = (1+401)/2 로 설정해야한다.
반대로 랜선의 개수가 N보다 크다면, 랜선을 더 길게 잘라야 한다.
랜선의 개수가 N과 같더라도 랜선의 길이는 더 길게 자를 수도 있기 때문에 랜선의 길이를 키워준다.

랜선의 개수가 N보다 크거나 같은 경우에는 answer라는 변수에 랜선의 길이를 대입해두는 것이 좋다.
B.S가 끝났을 때, answer에 저장되어있는 값이 가장 길었던 랜선의 길이가 될 것이기 때문이다.

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