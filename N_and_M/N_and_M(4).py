# 비 내림차순, 중복허용 순열 출력 (2,2),(2,3),(2,4),(3,3),(3,4) ..

def Permutation(arr, result, depth, index):
    if(depth==m):
        print(' '.join(str(e) for e in result))
        return
    else:
        for i in range(index, n):
            result[depth] = arr[i]
            Permutation(arr, result, depth+1, i)
    

n, m = map(int, input().split())
arr = list(range(1, n+1))
result=[0]*m
Permutation(arr, result, 0, 0)
