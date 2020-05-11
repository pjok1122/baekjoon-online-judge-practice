class Solution:
    def findJudge(self, N, trust):
        edges = [set() for i in range(N+1)]
        for t in trust:
            edges[t[0]].add(t[1])
        
        candidate = set(range(1,N+1))
        for i in range(1,N+1):
            if(len(edges[i])!=0):
                candidate = candidate.intersection(edges[i])
        
        if(len(candidate)==1):
            return candidate.pop()
        else:
            return -1

sol = Solution()
sol.findJudge(3, [[1,3],[2,3],[3,1]])
