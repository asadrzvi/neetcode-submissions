class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                row_val = board[i][j]
                if row_val != ".":
                    if row_val not in row_seen:
                        row_seen.add(row_val)
                    else:
                        return False
                
                col_val = board[j][i]
                if col_val != ".":
                    if col_val not in col_seen:
                        col_seen.add(col_val)
                    else:
                        return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_seen = set()
                for k in range(3):
                    for l in range(3):
                        box_val = board[i+k][j+l]
                        if box_val != ".":
                            if box_val not in box_seen:
                                box_seen.add(box_val)
                            else:
                                return False

        return True
