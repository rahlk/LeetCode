"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 
  - 'M' represents an unrevealed mine, 
  - 'E' represents an unrevealed empty square, 
  - 'B' represents a revealed blank square that has no adjacent (above, below, 
    left, right, and all 4 diagonals) mines, 
  - digit ('1' to '8') represents how many mines are adjacent to this revealed squ
  are, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the 
unrevealed squares ('M' or 'E'), return the board after revealing this position 
according to the following rules:

 - If a mine ('M') is revealed, then the game is over - change it to 'X'.
 - If an empty square ('E') with no adjacent mines is revealed, then change it 
   to revealed blank ('B') and all of its adjacent unrevealed squares should 
   be revealed recursively.
 - If an empty square ('E') with at least one adjacent mine is revealed, then 
   change it to a digit ('1' to '8') representing the number of adjacent mines.

Return the board when no more squares will be revealed.

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Note:
 1. The range of the input matrix's height and width is [1,50].
 2. The click position will only be an unrevealed square ('M' or 'E'), which 
    also means the input board contains at least one clickable square.
 3. The input board won't be a stage when game is over (some mines have been 
    revealed).
 4. For simplicity, not mentioned rules should be ignored in this problem. 
    For example, you don't need to reveal all the unrevealed mines when the game
    is over, consider any cases that you will win the game or flag any squares.
"""

from pdb import set_trace

class Solution(object):
    def updateBoard_rdfs(self, board, click):
        """
        A Recursive DFS approach. 
        We use a for loop, that pick the first neighbor and explores it.
        
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        if board[click[0]][click[1]] == "M":
            "If mine, just return board with 'X'"
            board[click[0]][click[1]] = "X"
            return board

        def neighbors(row, col):
            for r in xrange(-1, 2):
                for c in xrange(-1, 2):
                    if (0 <= row + r < len(board) and 0 <= col + c < len(board[0])) and (r or c):
                        yield row + r, col + c

        def explore(board, row, col, seen=[]):

            if not (row, col) in seen:
                "Add cell to explored"
                seen += [(row, col)]

                if not board[row][col] == "M":
                    "Look around for mine, but only if the cell is not a mine"
                    board[row][col] = 0  # initialize cell to 0 mines

                    "Look in all 8 directions for mines"
                    for r, c in neighbors(row, col):
                        if board[r][c] == "M":
                            board[row][col] += 1

                    "If the value of the cell is still zero then set to 'B'"

                    board[row][col] = "B" if board[row][col] == 0 else board[row][col]

                "Recurse on all the neighbors"
                for r, c in neighbors(row, col):
                    if not (r, c) in seen:
                        board = explore(board, r, c, seen)

            return board

        return explore(board, row=click[0], col=click[1])


    def updateBoard_nrbfs(self, board, click):
        """
        A non-recursive breadth first search approach. We must use queues. 
        
        Remember as 
          - queues -> horizontal -> breadth
          - stacks -> vertical -> depth
        
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        def neighbors(row, col):
            for r in [1, -1, 0]:
                for c in [0, 1, -1]:
                    if (0 <= row + r < len(board) and 0 <= col + c < len(
                            board[0])) and (r or c):
                        yield row + r, col + c

        "Create an empty queue to hold the next cell to explore"
        queue = deque()
        seen = []
        "If mine, just return board with 'X'"
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        else:
            queue.extend([tuple(click)])
            while len(queue):
                row, col = queue.pop()  # We're using queues, so pick left.
                seen.append((row, col))

                "Find if there are mines in the viscinity"
                board[row][col] = sum([int(board[r][c] == "M")
                                       for r, c in neighbors(row, col)])

                "If no. of mines is 0 then put 'B' else put the mine count"
                board[row][col] = "B" if board[row][col] == 0 else board[row][col]

                "Add all the neighbors of the cell to the queue"
                queue.extendleft([(r, c) for r, c in neighbors(
                    row, col) if (r, c) not in seen and board[r][c] == 'E'])

            return board


    def updateBoard_rbfs(self, board, click):
        """
        A recursive breadth first search approach. Uses queues recursively.
        
        Again, remember as:
          - queues -> horizontal -> breadth
          - stacks -> vertical -> depth

        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == "M":
            "If mine, just return board with 'X'"
            board[click[0]][click[1]] = "X"
            return board
        
        from collections import deque
        queue = deque()
        queue.append((click[0], click[1]))

        def neighbors(row, col):
            for r in xrange(-1, 2):
                for c in xrange(-1, 2):
                    if (0 <= row + r < len(board) and 0 <= col + c < len(board[0])) and (r or c):
                        yield row + r, col + c

        def explore(board, seen=[], next=queue):

            (row, col) = next.popleft()
            if board[row][col] == "E":
                "Add cell to explored"
                seen += [(row, col)]

                if not board[row][col] == "M":
                    "Look around for mine, but only if the cell is not a mine"
                    board[row][col] = 0  # initialize cell to 0 mines

                    "Look in all 8 directions for mines"
                    for r, c in neighbors(row, col):
                        if board[r][c] == "M":
                            board[row][col] += 1

                    "If the value of the cell is still zero then set to 'B'"

                    board[row][col] = "B" if board[row][col] == 0 else board[row][col]

                """
                This is the DFS part, since we use queues, 
                the next neighbors are dequeued leading to a dfs
                """
                next.extend([(r,c) for r, c in neighbors(row, col) if board[r][c]=="E"])
                
                board = explore(board, seen, next)

            return board

        return explore(board, next=queue)



def _test():
    s = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'M', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'M', 'E'],
             ['E', 'E', 'E', 'E', 'M']]

    print("Recursive DFS")
    board_1 = s.updateBoard_rdfs(board, click=[3, 0])
    for row in board:
        print(row)

    print("\n")
    print("Recursive BFS")
    board_1 = s.updateBoard_rbfs(board, click=[3,0])
    for row in board:
        print(row)

    print("\n")
    print("Non-Recursive BFS")
    board_1 = s.updateBoard_nrbfs(board, click=[3, 0])
    print(row)
    for row in board:
        print(row)

if __name__ == "__main__":
    _test()

