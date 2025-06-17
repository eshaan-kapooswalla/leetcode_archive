"""
Valid Parentheses (LeetCode #20)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Map of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            # If it's an opening bracket, push to stack
            if char in '({[':
                stack.append(char)
            # If it's a closing bracket
            elif char in ')}]':
                # If stack is empty or top of stack doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
                
        # Stack should be empty if all brackets are matched
        return len(stack) == 0
