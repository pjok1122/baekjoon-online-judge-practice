#데이터가 주어졌을 때, 중복순열
def OverlapPermutation(arr, result, depth, n, r):
    if(depth==r):
        print(' '.join(str(e) for e in result[:r]))
        return
    else:
        for i in range(n):
            result[depth] = arr[i]
            OverlapPermutation(arr, result, depth+1, n ,r)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result=[0]*n
OverlapPermutation(arr, result, 0, n, m)

