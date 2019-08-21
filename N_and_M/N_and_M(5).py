#데이터가 주어졌을 때, 순열 출력

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
    arr = list(map(int, input().split()))
    arr.sort()
    result = [0]*(n)
    permutation(arr, result, 0)
