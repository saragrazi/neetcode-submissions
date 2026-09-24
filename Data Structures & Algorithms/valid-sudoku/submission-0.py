class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_row = [[0] * 9 for _ in range(9)]
        list_col = [[0] * 9 for _ in range(9)]
        list_boxes = [[0] * 9 for _ in range(9)]
        curr_box = 0
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    curr_box = (i // 3) * 3 + (j // 3)
                    value = int(value) - 1
                    if list_row[i][value] == 1 or list_col[j][value] == 1 or list_boxes[curr_box][value] == 1:
                        return False
                    list_row[i][value] = 1 
                    list_col[j][value] = 1 
                    list_boxes[curr_box][value] = 1
        return True