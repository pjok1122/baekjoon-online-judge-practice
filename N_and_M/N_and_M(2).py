#조합

def combination(arr,depth, index):
    if(depth==m):
        print(' '.join(str(e) for e in result))
        return
    for i in range(index, n+1):
        result[depth] = arr[i]
        combination(arr, depth+1, i+1)


    
if __name__=="__main__":
    n,m = map(int,input().split())
    arr = list(range(n+1))
    result = [0]*m
    visited = [0]*(n+1)
    combination(arr,0, 1)
