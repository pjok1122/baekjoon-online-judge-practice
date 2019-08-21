# 비 내림차순, 중복허용 순열 출력 (2,2),(2,3),(2,4),(3,3),(3,4) ..
# 데이터 주어짐.

def Permutation(arr, result, depth, n, r):
    if(depth==r):
        print(' '.join(str(e) for e in result[:r]))
        return
    else:
        for i in range(n):
            result[depth] = arr[i]
            Permutation(arr[i:], result, depth+1, n-i, r)
    

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result=[0]*n
Permutation(arr, result, 0, n, m)
