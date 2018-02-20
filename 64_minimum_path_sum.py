"""
Given a m x n grid filled with non-negative numbers, find a path from top left 
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]

Given the above grid map, return 7. Because the path 1->3->1->1->1 minimizes the 
sum.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if i == 0 and 0 < j < len(grid[0]):
                    "This is the topmost row"
                    grid[i][j] += grid[i][j - 1]

                elif j == 0 and 0 < i < len(grid):
                    "This is the leftmost colum"
                    grid[i][j] += grid[i-1][j]

                elif 0 <= i-1 < len(grid) and 0 <= j-1 < len(gris[0]): 
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]

def _test():
    s = Solution()

    print s.minPathSum(grid=[[1, 3, 1],
                             [1, 5, 1],
                             [4, 2, 1]])

if __name__ == "__main__":
    _test()
