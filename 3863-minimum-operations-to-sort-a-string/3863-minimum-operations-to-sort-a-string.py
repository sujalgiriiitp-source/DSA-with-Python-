class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Check if already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        
        # Impossible case for length 2 (proper substring has length 1, so s can't change)
        if n == 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        # Case 1: Minimum character is already at the start OR Maximum character is at the end
        if s[0] == min_char or s[-1] == max_char:
            return 1
        
        # Case 3: Maximum is at the first index AND Minimum is at the last index
        # (and no other occurrences of min_char/max_char exist in the middle)
        if s[0] == max_char and s[-1] == min_char and min_char not in s[1:-1] and max_char not in s[1:-1]:
            return 3
        
        # Case 2: All other unsorted strings
        return 2