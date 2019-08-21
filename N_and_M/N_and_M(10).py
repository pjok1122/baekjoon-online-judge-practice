def Combination(arr,result, depth, n, m):
    if(depth==m):
        print(result)

    else:
        for i in range(n):
            result[depth]=arr[i]
            Combination(arr[i:], result, depth+1, n-i, m)

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result=[0]*m

Combination(arr,result,0,n,m)
