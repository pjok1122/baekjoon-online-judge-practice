def solution(N, stages):
    # N : 토탈 스테이지 수
    # stages : 사람들이 머물고 있는 스테이지
    ''' 아이디어 
    1. 스테이지 별로 사람 수를 cnt 배열에 저장. O(n)
    2. 분자 : cnt[i] , 분모 : 전체개수 - cnt[0] -cnt[1] ... - cnt[i-1]
    3. 실패율을 저장.
    4. 내림차순으로 정렬.

    실패율 : 스테이지 번호 + 해당 스테이지의 실패율 (스테이지 번호는 인덱스로 두자.)
    '''
    fail =[0]*(N+2)  #1탄부터 N+1탄까지 머무를 수 있음.
    cnt =[0]*(N+2)

    for stage in stages:
        cnt[stage]+=1
    
    sum_cnt = 0
    user = len(stages)
    for i in range(1, N+1):
        if cnt[i]==0:
            fail[i] = [i, 0]
            continue
        fail[i] = [i, cnt[i] / (user - sum_cnt)]
        sum_cnt += cnt[i]
    answer = sorted(fail[1:N+1], key= lambda x:(x[1]), reverse=True)
    answer = [stage[0] for stage in answer]
    # print(answer)
    return answer

if __name__=="__main__":
    # solution(5, [2,1,2,6,2,4,3,3])
    solution(4, [1])
    # solution