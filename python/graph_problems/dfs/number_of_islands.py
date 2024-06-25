from collections import deque

class Solution(object):

    def is_point_available(self, grid, sP, direction):
        if direction == "top":
            if sP[1] - 1 < 0:
                return False
            if grid[sP[0]][sP[1]-1] == "0":
                return False
        elif direction == "bottom":
            if sP[1] + 1 < 0 or sP[1] + 1 >= grid[0].__len__():
                return False
            if grid[sP[0]][sP[1]+1] == "0":
                return False
        elif direction == "left":
            if sP[0] - 1 < 0:
                return False
            if grid[sP[0]-1][sP[1]] == "0":
                return False
        elif direction == "right":
            if sP[0] + 1 < 0 or sP[0] + 1 >= grid.__len__():
                return False
            if grid[sP[0]+1][sP[1]] == "0":
                return False
        else:
            raise ValueError("Invalid direction")
        
        return True
            
    def perform_dsf(self, grid, sP):
        """
        @args: sP: starting Point
        
        """
        if grid[sP[0]][sP[1]] == "0":
            return
        
        grid[sP[0]][sP[1]] = "0"
        
        if self.is_point_available(grid, sP, "top"):
            self.perform_dsf(grid=grid, sP=(sP[0], sP[1]-1))
        
        if self.is_point_available(grid, sP, "bottom"):
            self.perform_dsf(grid=grid, sP=(sP[0], sP[1]+1))
        
        if self.is_point_available(grid, sP, "left"):
            self.perform_dsf(grid=grid, sP=(sP[0]-1, sP[1]))
        
        if self.is_point_available(grid, sP, "right"):
            self.perform_dsf(grid=grid, sP=(sP[0]+1, sP[1]))


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands_count = 0
        
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if int(grid[x][y]):
                    islands_count += 1
                    self.perform_dsf(grid=grid, sP=(x, y))

        print("islands_count", islands_count)
        return islands_count
                

if __name__=="__main__":
    grid = [
        ["1","1","1","1","1"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    solution = Solution()
    solution.numIslands(grid)
