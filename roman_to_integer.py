# Solution for LeetCode problem: Roman To Integer

def solution():
    """
    Roman to Integer (LeetCode 13).
    Usage: Call romanToInt(s) where s is a Roman numeral string.
    Returns the integer value of the Roman numeral.
    """
    def romanToInt(s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for char in reversed(s):
            value = roman[char]
            if value >= prev:
                total += value
            else:
                total -= value
            prev = value
        return total
    # Example usage:
    # print(romanToInt("MCMXCIV")) # Output: 1994
    pass
