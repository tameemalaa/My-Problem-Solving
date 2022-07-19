class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visted = []
        max_area= 0
        def find_area(i,j):
            if grid[i][j]:
                accumlator=1
                visted.append((i,j))
                if i !=0 and (i-1,j) not in visted:
                    accumlator+= find_area(i-1,j)
                if j !=0 and (i,j-1) not in visted:
                    accumlator+= find_area(i,j-1)
                if i != len(grid)-1 and (i+1,j) not in visted:
                    accumlator+= find_area(i+1,j)
                if j != len(grid[i])-1 and (i,j+1) not in visted:
                    accumlator+= find_area(i,j+1)
                return accumlator
            else : return 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i,j) not in visted :
                    max_area = max(max_area,find_area(i,j))
        return max_area