class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        # Iteration for space skipping
        while i >= 0 and s[i] == ' ':
            i -= 1
        # Iteration for word counts
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length