# Solution for LeetCode problem: Maximal Square

def solution():
    """
    Maximal Square (LeetCode 221).
    Usage: Call maximalSquare(matrix) where matrix is a List[List[str]] of '0' and '1'.
    Returns the area of the largest square containing only 1's.
    """
    def maximalSquare(matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len
    # Example usage:
    # matrix = [
    #   ["1","0","1","0","0"],
    #   ["1","0","1","1","1"],
    #   ["1","1","1","1","1"],
    #   ["1","0","0","1","0"]
    # ]
    # print(maximalSquare(matrix)) # Output: 4
    pass
