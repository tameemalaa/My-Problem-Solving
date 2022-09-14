class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visted = set()
        def check_island(i,j):
            if grid[i][j] == "1" :
                visted.add((i,j))
                if i !=0 and (i-1,j) not in visted: check_island(i-1,j)
                if j !=0 and (i,j-1) not in visted: check_island(i,j-1)
                if i != len(grid)-1 and (i+1,j) not in visted: check_island(i+1,j)
                if j != len(grid[i])-1 and (i,j+1) not in visted: check_island(i,j+1)
                return 1
            else : return 0
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i,j) not in visted and grid[i][j]=='1' :
                    n += check_island(i,j)
        return n