from typing import List

class Solution:

    def is_within_bounds(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
            
    def perform_dfs(self, grid: List[List[str]], x: int, y: int) -> None:
        """
        Perform Depth-First Search (DFS) to mark all connected land (1s) as visited (0s).
        """
        if not self.is_within_bounds(grid, x, y) or grid[x][y] == "0":
            return
        
        grid[x][y] = "0"  # Mark the current point as visited by setting it to "0"

        # List of direction vectors for moving top, bottom, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            self.perform_dfs(grid, x + dx, y + dy)

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands in the given grid.
        :type grid: List[List[str]]
        :rtype: int
        """
        islands_count = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    islands_count += 1
                    self.perform_dfs(grid=grid, x=x, y=y)

        return islands_count
                

if __name__=="__main__":
    grid = [
        ["1","1","1","1","1"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)  # Output: 1
