class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visted = set()
        def check_island(i,j):
            if grid[i][j] == 0 :
                visted.add((i,j))
                ans = 1 
                if i ==0 or i == len(grid)-1 or j==0 or j== len(grid[i])-1 : ans= 0 
                sides= set()
                if i !=0 and (i-1,j) not in visted: sides.add(check_island(i-1,j))
                if j !=0 and (i,j-1) not in visted: sides.add(check_island(i,j-1))
                if i != len(grid)-1 and (i+1,j) not in visted: sides.add(check_island(i+1,j))
                if j != len(grid[i])-1 and (i,j+1) not in visted: sides.add(check_island(i,j+1))
                return 0 if not(sides) or 0 in sides else min(ans,1)

        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visted and grid[i][j]==0 :
                    n += check_island(i,j)
        return n