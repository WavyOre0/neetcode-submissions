class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #you need to keep a hashset that checks for duplicate numbers in each row and column
        # you need to figure out how to get each box and check if there is a duplicate in it
        # not all the numbers are filled in so only go based off the present numbers.

        val_row = collections.defaultdict(set) # you want the key of the map to be a set 
        val_col = collections.defaultdict(set)
        val_sq = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in val_row[r] or
                    board[r][c] in val_col[c] or 
                    board[r][c] in val_sq[(r//3,c//3)]):
                    return False
                val_row[r].add(board[r][c])
                val_col[c].add(board[r][c])
                val_sq[(r//3,c//3)].add(board[r][c])
        return True
