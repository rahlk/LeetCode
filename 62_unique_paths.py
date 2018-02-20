"""
A robot is located at the top - left corner of a m x n grid.

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom - right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


from collections import deque
from pdb import set_trace

class Solution(object):
    def uniquePaths(self, m, n):
        """
        A non recursive BFS/DFS approach. Seems to be very slow for large matrices

        :type m: int
        :type n: int
        :rtype: int
        """

        board = m * [n* [0]]
        board[m-1][n-1] = "G" # Goal

        def neighbors(row, col):
            "Gives you a neighbor -> right cell or a down cell"
            for r in xrange(2):
                for c in xrange(2):
                    if (0 <= row + r < m and 0 <= col + c < n) and (r ^ c):
                        yield row + r, col + c

        queue = deque()
        queue.append((0, 0))
        uniq_paths = 0
        
        while len(queue) > 0:
            (row, col) = queue.pop()
            if board[row][col] == "G":
                    uniq_paths += 1
                
            else:
                "Look at neighbors"
                queue.extend([(r, c) for r, c in neighbors(
                    row, col)])

        return uniq_paths

    def uniquePaths_recr(self, m, n):
        """
        A recursive approach.

        :type m: int
        :type n: int
        :rtype: int
        """
        uniq_paths = 0

        def explore(row, col, uniq_paths):
            if 0<=row<m and 0<=col<n:
                if row == m-1 and col == n-1:
                    uniq_paths += 1
                else:
                    uniq_paths = explore(row + 1, col, uniq_paths) 
                    uniq_paths = explore(row, col + 1, uniq_paths)
            return uniq_paths
        
        return explore(0,0,uniq_paths)

    def uniquePaths_dprog(self, m, n):
        """
        A dynamic programming approach

        :type m: int
        :type n: int
        :rtype: int
        """
        board = [n*[1]]

        for row in xrange(1, m):
            new_row = n * [1]
            for col in xrange(1, n):
                new_row[col] = board[row-1][col] + new_row[col-1]
            board.append(new_row)

        return board[m-1][n-1]
                


def _test():
    s = Solution()
    print s.uniquePaths_dprog(12,23)

if __name__ == "__main__":
    _test()
