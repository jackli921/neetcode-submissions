class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                v = board[row][col]
                if v in rows[row] or v in cols[col] or v in boxes[(row // 3, col // 3)]:                
                    return False
                rows[row].add(v)
                cols[col].add(v)
                boxes[(row//3,col//3)].add(v)
        
        return True