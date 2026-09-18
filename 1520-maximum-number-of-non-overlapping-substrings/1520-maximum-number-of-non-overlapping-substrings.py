class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: s.find(c) for c in set(s)}
        last = {c: s.rfind(c) for c in set(s)}
        
        intervals = []
        
        for c in first:
            l, r = first[c], last[c]
            valid = True
            
            i = l
            while i <= r:
                char = s[i]
                if first[char] < l:
                    valid = False
                    break
                r = max(r, last[char])
                i += 1
                
            if valid:
                intervals.append((r, l))
                
        intervals.sort()
        res, prev_end = [], -1
        
        for r, l in intervals:
            if l > prev_end:
                res.append(s[l:r + 1])
                prev_end = r
                
        return res
        