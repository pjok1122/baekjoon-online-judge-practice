'''
정답률 : 16.09%
1. 데이터가 적기 때문에 생각나는대로 조합해도 괜찮음. (복잡도 연연하지 않는 문제)
2. 1단계 : relation에서 원하는 컬럼만을 뽑아서 집합을 구성하고, 그 갯수가 줄어들지 않았다면 키 후보
3. 2단계 : 키 후보에서 최소성을 만족해야 하는데, 0001이 키인 경우 0011, 0101 1001 모두 키가 될 수 없음.
4. 3단계 : 그 과정을 논리적으로 나타내면 (키) & (키후보) == (키) 라는 방정식이 나옴을 알 수 있음. 

'''
def solution(relation):
    check = 1<<len(relation[0])
    cand =[]
    key =[]

    for i in range(1, check):   #1111 : 모든 컬럼을 사용
        Set = set()
        for k in range(len(relation)):  #row의 갯수만큼,
            tmp=''
            for j in range(len(relation[0])): #해당되는 컬럼만 뽑아서 리스트로 저장한 후, 전체 리스트에 저장.
                if (i>>j)&1:
                    tmp += str(relation[k][j])
            Set.add(tmp)

        if len(Set) == len(relation):
            cand.append(i)
            
    for c in cand:
        is_key =True
        for k in key:
            if k&c == k:
                is_key = False
                break
        if is_key:
            key.append(c)
    
    return len(key)

# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

# solution(relation)