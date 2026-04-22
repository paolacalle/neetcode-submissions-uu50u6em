class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the column to determine what row to binary search 
        n_cols, n_rows = len(matrix[0]), len(matrix)

        # First binary search over the rows
        l, r = 0, n_rows - 1
        m_row = None
        while l <= r: 
            m_row = l + (r - l) // 2
            lower_bound, upper_bound = matrix[m_row][0], matrix[m_row][-1]

            if lower_bound == target or upper_bound == target:
                return True
            elif lower_bound < target < upper_bound:
                break
            elif lower_bound > target: 
                r = m_row - 1
            else: 
                l = m_row + 1

        if not (l <= r):
            return False

        # Then binary search inside one row over the columns
        l, r = 0, n_cols - 1
        while l <= r:
            m_col = l + (r - l) // 2
            if matrix[m_row][m_col] == target:
                return True
            elif matrix[m_row][m_col] > target: 
                r = m_col - 1
            else: 
                l = m_col + 1

        return False

# Time complexity: O(log m + log n)
# - m = number of rows
# - n = number of columns


        

    