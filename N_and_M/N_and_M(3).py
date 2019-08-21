#중복순열
def OverlapPermutation(arr, result, depth):
    if depth==m:
        print(' '.join(str(e) for e in result))
        return
    else:
        for i in range(n):
            result[depth] = arr[i]
            OverlapPermutation(arr, result, depth+1)


n, m = map(int, input().split())
arr = list(range(1, n+1))
result=[0]*m
OverlapPermutation(arr, result, 0)

