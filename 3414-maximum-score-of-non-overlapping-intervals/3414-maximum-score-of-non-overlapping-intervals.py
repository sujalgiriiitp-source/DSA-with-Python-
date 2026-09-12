from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Sort original indices by their right endpoint to easily find non-overlapping ones
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rights = [intervals[i][1] for i in order]
        
        # We will store states as (negative_score, sorted_indices).
        # k = 0: nothing picked yet
        prev = [(0, [])] * (n + 1) 
        
        # We can pick up to 4 intervals
        for _ in range(4):
            cur = [(0, [])] * (n + 1)
            for p in range(1, n + 1):
                i = order[p - 1] 
                l, r, w = intervals[i]
                
                # Find the rightmost interval that ends strictly before `l`
                j = bisect_left(rights, l) 
                
                score, ids = prev[j]
                
                # The trick: store score as negative (`score - w`). 
                # This way, Python's `min()` naturally minimizes the negative score (maximizing the real score),
                # and if scores tie, it falls back to comparing `sorted(ids + [i])` lexicographically!
                cur[p] = min((score - w, sorted(ids + [i])), cur[p - 1])
                
            prev = cur
            
        # Return the indices of the final optimal state
        return prev[n][1]