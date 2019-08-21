#순열
def permutation(arr, result, depth):
    if(depth==m):
        print(' '.join(str(e) for e in result))
        return
    for i in range(n-depth):
        result[depth] = arr.pop(i)
        permutation(arr,result, depth+1)
        arr.insert(i, result[depth])

if __name__=="__main__":
    n,m = map(int,input().split())
    arr = list(range(1,n+1))
    result = [0]*m
    permutation(arr, result, 0)
    
