# Solution for LeetCode problem: Regular Expression

def solution():
    """
    Implements regular expression matching with support for '.' and '*'.
    Example usage:
    result = isMatch(s, p)
    """
    def isMatch(s: str, p: str) -> bool:
        rows, columns = (len(s), len(p))
        dp = [[False] * (columns + 1) for _ in range(rows + 1)]
        dp[0][0] = True
        for i in range(2, columns + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[rows][columns]
    # Example usage:
    # print(isMatch("aa", "a*")) # returns True
    pass
