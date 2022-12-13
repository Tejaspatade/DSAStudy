
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # No. of rows
        rows = len(matrix)
        # DP recursive
        def dp(row, col, dpMemo):
            # Base Case for out of bounds pointers
            if row < 0 or col < 0 or row > rows-1 or col > rows-1:
                # Return Highest Possible value to cancel out in parent min() comparison
                return float('inf')
            # Base Case for last row elements
            if row == rows-1:
                return matrix[row][col]
            # Check for subproblem in memo
            if dpMemo[row][col] != -1: return dpMemo[row][col]
            
            # Move Down, Left & Right
            down = matrix[row][col] + dp(row+1, col, dpMemo)
            rdiag = matrix[row][col] + dp(row+1, col+1, dpMemo)
            ldiag = matrix[row][col] + dp(row+1, col-1, dpMemo)
            
            # Store sub-problem in memo for future use
            dpMemo[row][col] = min(down, rdiag, ldiag)
            return dpMemo[row][col]
        
        # Start from infinity and find smallest sum starting from each of num in 1st row
        output = float('inf')
        dpMemo = [[-1]*rows for _ in range(rows)]
        for j in range(rows):
            output = min(output, dp(0, j, dpMemo))
        return output