# 데이터가 적기 때문에 생각나는대로 조합해도 괜찮음.
def solution(relation):
    check = 2**len(relation[0])
    cand =[]
    key =[]
    
    for i in range(1, check):   #1111 : 모든 컬럼을 사용
        result = []
        Set = set()
        for k in range(len(relation)):  #row의 갯수만큼,
            row =[]
            for j in range(len(relation[0])): #해당되는 컬럼만 뽑아서 리스트로 저장한 후, 전체 리스트에 저장.
                if (i>>j)&1:
                    row.append(relation[k][j])
            result.append(row)
        
        #중복확인
        for k in range(len(result)):
            Set.add(''.join(result[k]))
        if len(Set) == len(result):
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