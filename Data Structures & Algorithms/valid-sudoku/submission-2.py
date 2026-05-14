class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        freq = defaultdict(int)

        #check rows
        for row in board:
            freq.clear()
            for num in row:
                if num == '.': continue
                freq[num] += 1
                if freq[num] > 1:
                    return False

        #check cols
        for c in range(9):
            freq.clear()
            for r in range(9):
                num = board[r][c]
                if num == '.': continue
                freq[num] += 1
                if freq[num] > 1:
                    return False

        # check by squar
        for r in range(3):
            for i in range(3):
                freq.clear()
                for j in range(3):
                    for x in range(3):
                        if(board[(r*3) + j][(i*3) + x] == '.') : continue
                        freq[board[(r*3) + j][(i*3) + x]] += 1
                        
                        if freq[board[(r*3) + j][(i*3) + x]] > 1:
                            return False
        
        return True