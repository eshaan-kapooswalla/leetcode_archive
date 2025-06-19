# Solution for LeetCode problem: Palindrome Number

def solution():
    """
    Palindrome Number (LeetCode 9).
    Usage: Call isPalindrome(x) where x is an integer.
    Returns True if x is a palindrome, False otherwise.
    """
    def isPalindrome(x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        return x == reverted or x == reverted // 10
    # Example usage:
    # print(isPalindrome(121)) # Output: True
    # print(isPalindrome(-121)) # Output: False
    pass
