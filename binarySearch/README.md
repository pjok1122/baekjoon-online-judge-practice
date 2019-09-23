## Binary Search

 이진탐색은 정렬된 데이터에 대해서 log(N) 복잡도를 가지는 탐색 기법입니다.

 단순히 원하는 값을 찾으면 멈추는 알고리즘도 있지만, 최대 인덱스나 최소 인덱스를 찾는 요령을 익혀두는 것이 좋습니다.
 
 1. Python 참고 라이브러리 : bisect

 2. 메소드 : bisect_left, bisect_right

## 소스 코드

```python
# 값을 찾으면 즉시 종료하는 Version (Yes/No 문제에 적합.)
def binarySearch_R(s,e,target):
    m = (s+e)//2

    #베이스 케이스
    if arr[m] == target:
        return 1
    elif s>=e:
        return 0
    elif arr[m] < target:
        return binarySearch_R(m+1,e,target)
    elif arr[m] > target:
        return binarySearch_R(s,m-1,target)

# for문을 이용한 풀이
def binarySearch(target):
    s = 0
    e = len(arr) - 1

    while (s<=e):
        m = (s+e)//2
        if arr[m] == target:
            return 1
        elif arr[m] < target:
            s = m + 1
        elif arr[m] > target:
            e = m - 1
    
    return 0
```

m을 확인한 후, 탐색 범위를 :m-1, m+1: 로 두기 때문에 무한루프에 빠질 걱정을 안해도 됩니다.

```python
# 값을 찾은 경우, 최대인덱스 또는 최소 인덱스를 출력하는 Version
# Iterative(Find max index)
def binarySearch(target):
    s = 0
    e = len(arr) - 1
    ans = -1
    while (s<=e):
        m = (s+e)//2
        if arr[m] <= target:
            ans = m
            s = m + 1
        elif arr[m] > target:
            e = m - 1
    return ans
```

ans 값을 업데이트 하여 최종적으로 ans를 반환하기 때문에 최대나 최소를 찾을 수 있습니다.

```python
#bisect는 binarySearch를 이용하여 해당 값을 어떤 인덱스에 삽입해야 하는지를 알려줍니다.

import bisect
a =[1,3]

print(bisect.bisect_left(a,1))
print(bisect.bisect_right(a,1,0,len(a)-1))

print(bisect.bisect_left(a,2))
print(bisect.bisect_right(a,2,0,len(a)-1))

'''
1. bisect는 정렬된 배열이 있을 때 x라는 값을 어디에 삽입할지 결정해주는 모듈이다.
2. 배열 a = [1,2,2,4,5]가 있다고 하자.
3. bisect_left(a,3) => 3을 반환, binsect_left(a,2) => 1을 반환
4. bisect_right(a,2) => 3을 반환 (그 이유는 3이라는 데이터를 삽입할 위치를 반환하기 때문.)
'''
```
