class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            None
        else:
            #print len(board),len(board[0])
            for i in range(len(board[0])):
                if board[0][i] == "O":self.dfs(board,0,i)
                if board[len(board)-1][i] == "O":self.dfs(board,len(board)-1,i)

            for i in range(len(board)):
                if board[i][0] == "O":self.dfs(board,i,0)
                if board[i][len(board[0])-1] == "O":self.dfs(board,i,len(board[0])-1)
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c]=="+":board[r][c]="O"
                    elif board[r][c]=="O":board[r][c]="X"

    def dfs(self,board,r,c):
        board[r][c] = "+"
        dir = [[0,-1],[-1,0],[0,1],[1,0]]
        for x,y in dir:
            row = r+x ; col = c+y
            if 0<=row<len(board) and 0<=col<len(board[0]) and board[row][col]=="O":
                self.dfs(board,row,col)
            
