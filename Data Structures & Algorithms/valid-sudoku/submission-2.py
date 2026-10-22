class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue                
                if v not in rows[r] and v not in cols[c] and v not in box[(r // 3, c // 3)]:
                    rows[r].add(v)
                    cols[c].add(v)
                    box[(r//3,c//3)].add(v)
                else:
                    return False
        return True