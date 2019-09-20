'''
[문제 풀기 전 생각할 것]

기타줄 6묶음(패키지) 가격이 낱개로 구매하는 것보다 저렴한지 파악해야 한다.

만약 패키지가 저렴하다면, 6의 배수만큼 기타줄을 구매하고, 나머지 부분은 낱개 중 가장 저렴한 요금으로 구매하는 것이 좋다.

만약 패키지보다 낱개가 저렴하다면, 필요한 개수 전부를 낱개로 구매하는 것이 바람직하다.

[알고리즘]

1. 입력으로부터 가장 저렴한 패키지 가격과 가장 저렴한 낱개 가격을 저장한다. 
2. 패키지로 구매하는 것이 저렴한지, 낱개로 구매하는 것이 저렴한지 비교한다.
3. 낱개로 구매하는 것이 저렴하다면, 필요한 기타줄을 낱개로 전부 구매한다.
4. 패키지로 구매하는 것이 저렴하다면, 6의 배수만큼 패키지로 구매한다.
5. 남은 기타줄의 개수를 패키지로 구매하는 것이 저렴한지, 낱개로 구매하는 것이 저렴한지 판단한다.

[알고리즘 예시]

필요 기타 줄 : 17개
패키지 가격 : 12
낱개 가격 : 3

1. 낱개로 6개를 구매하면 18원이고, 패키지는 12원이므로 패키지로 구매하는 것이 바람직하다.
2. 기타줄 12개는 패키지로 구매하여, 남은 기타줄은 5개가 된다.     (+24원)
3. 남은 기타줄 5개를 낱개로 구매할 경우 15원이지만, 패키지로 구매할 경우 12원이다.
4. 따라서 패키지로 구매하는 것이 저렴하다.      (+12원)
5. 따라서 최종 비용은 36원이 된다.

'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
min_package = 1000
min_piece = 1000

#1. 최소 패키지 가격 & 최소 낱개 가격을 찾는다.
for i in range(M):
    pack, piece = map(int, input().split())
    if pack < min_package:
        min_package = pack
    if piece < min_piece:
        min_piece = piece

#2. 낱개로 구매하는 것과 패키지로 구매하는 비용을 비교한다.
if min_package>=6*min_piece:
    print(min_piece*N)
else:
    result = min_package*(N//6)
    remain = N % 6
    if min_package > min_piece * remain:
        result += min_piece * remain
    else:
        result += min_package
    
    print(result)