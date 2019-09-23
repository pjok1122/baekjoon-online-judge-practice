# N and M

 재귀함수와 백트래킹을 공부할 수 있는 가장 좋은 문제집입니다.

 라이브러리를 사용하여 구현할 수 있지만 직접 구현해보는 것이 좋습니다.

 Python 참고 라이브러리 : itertools

 모듈 : permutations, combinations 

## 기본 소스 코드

 ```python
 #순열
def permutation(arr, result, depth):
    if(depth==m):
        print(' '.join(str(e) for e in result))
        return
    for i in range(n-depth):
        result[depth] = arr.pop(i)
        permutation(arr,result, depth+1)
        arr.insert(i, result[depth])

 #조합
def combination(arr,depth, index):
    if(depth==m):
        print(' '.join(str(e) for e in result))
        return
    for i in range(index, n+1):
        result[depth] = arr[i]
        combination(arr, depth+1, i+1)

# Itertools library 사용.
import itertools
arr=['A','B','C','D']
print(list(itertools.permutations(arr,4)))
print(list(itertools.combinations(arr,4)))
 ```