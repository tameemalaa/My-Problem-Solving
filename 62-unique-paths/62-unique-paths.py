class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        w= dict()
        def paths(x,y):
            if x == 0 or y ==0 :
                w[(x,y)] = 1
                return w[(x,y)]
            if (x,y) in w.keys():
                return w[(x,y)]
            w[(x,y)] = paths(x-1,y) + paths(x,y-1)
            return w[(x,y)]
        return paths(n-1,m-1)