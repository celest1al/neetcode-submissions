class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [[False] * 9 for _ in range(9)]
        col_seen = [[False] * 9 for _ in range(9)]
        box_seen = [[False] * 9 for _ in range(9)]

        for row_idx in range(9):
            for col_idx in range(9):
                cell_value = board[row_idx][col_idx]

                if cell_value == ".":
                    continue
                
                # zero based
                digit_idx = int(cell_value) - 1 

                box_idx = (row_idx // 3) * 3 + (col_idx // 3)

                if row_seen[row_idx][digit_idx] or col_seen[col_idx][digit_idx] or box_seen[box_idx][digit_idx]:
                    return False
                
                row_seen[row_idx][digit_idx] = True
                col_seen[col_idx][digit_idx] = True
                box_seen[box_idx][digit_idx] = True
        
        return True