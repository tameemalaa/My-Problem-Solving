class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        g = {i : [] for i in range(1,n+1)}
        t = {i : [] for i in range(1,n+1)}
        for i in trust : 
            g[i[1]].append(i[0])
            t[i[0]].append(i[1])
        for i in g.keys():
            if len(g[i]) == n-1 and len(t[i]) == 0 :
                return i
        return -1
        