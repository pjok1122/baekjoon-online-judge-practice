'''
[문제 풀기에 앞서 생각할 것]

1. 톱날의 높이가 낮을 수록 더 많은 나무를 벨 수 있다.
2. 문제 '톱날의 높이'를 Binary Search를 이용하여 찾아 나간다.
3. 톱날의 높이가 결정되었을 때, M 미터보다 크거나 같으면, 톱날의 높이 H를 높여준다. (같을 때 톱날의 높이를 높여주는 것이 핵심.)
                              M 미터보다 작으면, 톱날의 높이 H를 낮춰준다.

[B.S 알고리즘]

문제의 예시처럼 [10,15,17,20] 높이에 해당하는 나무가 있다고 하자.

톱날의 최소 높이는 0이 될 수 있으며, 최대 높이는 20이다.

즉, 우리가 원하는 답은 0~20 사이에 존재한다.

B.S를 적용하기 위해 mid = (0+20)/2 ---> 10으로 설정하자.

즉 톱날의 높이가 10일 때, 가져갈 수 있는 나무의 양을 계산해야 한다.

따라서 가져갈 수 있는 나무의 양을 계산하는 알고리즘을 작성한다.


[가져갈 수 있는 나무 계산 알고리즘]

예시 : [10,15,17,20]

1. 나무의 높이가 톱날의 높이보다 높은 경우에만 나무를 가져갈 수 있다.
2. 따라서 그런 경우에, Sum += 나무 높이 - 톱의 높이 = tree[i] - height 로 계산한다.
3. 결과를 return한다.
----------------------------------------------------------------------------------

mid = 10일 때 나무 계산 알고리즘을 사용하면 5+7+10 = 22의 나무를 가져갈 수 있다.
이는 목표했던 M = 7보다 크기 때문에 톱의 높이를 더 높여줘야 한다.
반대로 나무의 양이 M보다 작다면 톱의 높이를 낮춰줘야 한다.
만약 나무의 양이 M과 동일하다면 어떻게 해야할까? 나무의 양이 M과 동일하더라도 톱의 높이를 높여보는 것이 바람직하다.

나무의 높이가 M보다 크거나 같을 때가 정답이 될 수 있으므로 톱의 높이를 ans라는 변수에 계속 저장해두는 것이 좋다.

'''

N,M = map(int,input().split())
tree = list(map(int,input().split()))

# 원하는 나무의 양을 target에 대입.
# start, mid , end := 톱의 높이
def treeSum(height):
    Sum = 0
    for i in tree:
        if i-height >0:
            Sum+=(i-height)

    return Sum

def binarySearch(target):
    start,end=0, max(tree)
    ans = 0
    while(start<=end):
        mid = (start+end)//2
        Sum = treeSum(mid)
        if Sum < target :
            end = mid -1
        if Sum >= target:
            ans = mid
            start = mid + 1

    return ans

print(binarySearch(M))