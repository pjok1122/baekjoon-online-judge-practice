def solution(n,weak,dist):
    answer = 0

    while True:
        length = len(weak)
        if length==0:
            return answer
        if length==1 and len(dist)>1 and dist[-1]>=1:
            return answer+1
        
        result=[]
        for i in range(length):
            distance=0
            j=i+1
            while distance<dist[-1]:
                if i==j:
                    break
                if (i<j) and j%:
                    distance = (weak[j]-weak[i])
                else:
                    distance = (weak[j%length]+n-weak[i])
                j+=1    
                j%=length
            
            if i==j:
                remain =0
            elif (i-1)%length ==j:
                remain = 1
            else:
                remain = (weak[i-1]-weak[j])%n
            result.append([i,j-1,remain])
        result.sort(key=lambda x:x[2])
        return result


# def solution(n, weak, dist):
#     answer = 0
#     while True:
#         length = len(weak)
#         start,end =0,0
#         Min = dist[-1]
#         if length==0:
#             return answer
        
#         if len(dist)==0:
#             return -1
        
#         #한 번에 끝낼 수 있는 업무의 길이를 찾는다.
#         for i in range(1,length):
#             flag = 1
#             for j in range(length):
#                 distance = (weak[(i+j)%length] - weak[j]) % n
#                 if 0<= (dist[-1]-distance) <= Min:
#                     flag = 0
#                     Min = dist[-1]-distance
#                     start,end = j, (i+j)%length
            
#             if flag: #더 이상 만족하는 거리가 안나오면 종료
#                 break
            
#         if start>end:
#             weak = weak[end:start]
#         elif start<=end:
#             del(weak[start:end+1])
        
#         answer +=1
#         del(dist[-1])
        
                    

    return answer


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12,[1,3,4,9,10],[3,5,7]))