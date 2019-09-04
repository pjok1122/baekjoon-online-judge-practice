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