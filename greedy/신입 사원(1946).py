'''
[문제 풀기 전 생각할 것]

서류 또는 면접에서 1등한 사람은 반드시 선발된다는 사실을 알 수 있다.

편의를 위해 서류 성적이 1등인 사람을 먼저 선발했다고 가정해보자.

서류 성적이 2등인 사람이 선발되기 위해서는, 서류1등보다 면접 성적이 높으면 된다.

따라서 서류 2등은 딱 1번의 비교만으로 선발 유무 파악이 가능하다.

서류 3등은, 서류 1등과 서류 2등 중에서 면접 성적이 높은 사람보다 면접 점수가 높으면 선발된다.

[알고리즘]

예시 : [[1,4], [2,3] ,[3,2] , [4,1] , [5,5]]
1. 주어진 점수를 서류 점수 기준으로 오름차순 정렬한다.
2. 서류 1등을 우선적으로 선발하고, 인터뷰 등수를 4로 저장한다.
3. 서류 2등의 인터뷰 등수는 3등이므로, 현재 인터뷰 등수(`4`)보다 높다. 따라서 신입 사원으로 선발한 후, 인터뷰 등수를 3으로 저장한다.
4. 서류 3등의 인터뷰 등수는 2등이므로, 현재 인터뷰 등수(`3`)보다 높다. 따라서 신입 사원으로 선발한 후, 인터뷰 등수를 2로 저장한다.
5. 서류 4등의 인터뷰 등수는 1등이므로, 현재 인터뷰 등수(`2`)보다 높다. 따라서 신입 사원으로 선발한 후, 인터뷰 등수를 1로 저장한다.
6. 서류 5등의 인터뷰 등수는 5등이므로, 현재 인터뷰 등수(`1`)보다 낮다. 따라서 선발하지 않는다.

현재 시간복잡도는 정렬과 비교 연산으로 나뉜다.
정렬의 시간복잡도 : O(nlogn)
for문 비교의 시간 복잡도 : O(n)

따라서 전체 시간복잡도는 : O(nlogn) 이다.

[효율적 알고리즘]

서류 등수는 결국 1등부터 N등까지 존재한다. 따라서 서류 등수를 index로 하는 배열을 생성하면 정렬에 필요한 시간복잡도를 제거할 수 있다.
ex) score['서류 등수'] = '면접 등수'

과정은 위와 동일하다.

시간 복잡도 : O(n)
'''
import sys

T = int(sys.stdin.readline())

# 알고리즘 1
# for test_case in range(T):
#     N = int(sys.stdin.readline())
#     scores = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#     scores.sort(key=lambda x: x[0])
    
#     ans = 1
#     interview_score = scores[0][1]

#     for score in scores[1:]:
#         if score[1] < interview_score:
#             ans+=1
#             interview_score = score[1]
    
#     print(ans)

# 알고리즘 2 (Optimization Version)
# 편의상 스코어 = 등수로 생각.
for test_case in range(T):
    N = int(sys.stdin.readline())
    scores =[100]* (N+1)
    for _ in range(N):
        i,j = map(int,sys.stdin.readline().split()) 
        scores[i]=j
    ans = 1
    interview_score = scores[1]

    for score in scores[2:]:
        if score < interview_score:
            ans+=1
            interview_score = score

    print(ans)