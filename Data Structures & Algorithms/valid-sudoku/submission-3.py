class Solution:

    def isValidRows(self, board: List[List[str]]) -> bool:
        print("ROW")

        for row in range(0, 9):
            seen = set()
            for col in range(0, 9):
                v = board[row][col]
                if v == '.':
                    continue

                if v in seen:
                    return False

                seen.add(v)

        return True

    def isValidCols(self, board: List[List[str]]) -> bool:
        print("COLS")
        for col in range(0, 9):
            seen = set()
            for row in range(0, 9):
                v = board[row][col]
                if v == '.':
                    continue

                if v in seen:
                    return False

                seen.add(v)
            print(".  ", seen)
                
        return True
            

    def isValidSubbox(self, board: List[List[str]]) -> bool: 
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for c in range(col, col + 3, 1):
                    for r in range(row, row + 3, 1):
                        v = board[r][c]

                        if v == '.':
                            continue
                        
                        if v in seen:
                            return False

                        seen.add(v)

            col += 3

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = self.isValidRows(board)
        c = self.isValidCols(board)
        b = self.isValidSubbox(board)
        print("R: ", r, "C: ", c, "B: ", b)

        return (True == r == c == b)

        