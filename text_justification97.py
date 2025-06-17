"""
Text Justification (LeetCode #68)

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters
and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Time Complexity: O(n * maxWidth) where n is the number of words
Space Complexity: O(n * maxWidth) for the result
"""

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding this word would exceed maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # Justify the current line
                if len(current_line) == 1:
                    # Left justify if only one word
                    result.append(current_line[0] + ' ' * (maxWidth - current_length))
                else:
                    # Calculate spaces between words
                    spaces = maxWidth - current_length
                    space_between = spaces // (len(current_line) - 1)
                    extra_spaces = spaces % (len(current_line) - 1)
                    
                    # Build the justified line
                    line = []
                    for i, w in enumerate(current_line):
                        line.append(w)
                        if i < len(current_line) - 1:
                            line.append(' ' * (space_between + (1 if i < extra_spaces else 0)))
                    result.append(''.join(line))
                
                # Start new line
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
        
        # Handle the last line (left justified)
        if current_line:
            last_line = ' '.join(current_line)
            result.append(last_line + ' ' * (maxWidth - len(last_line)))
            
        return result
