class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1
        
        for i in range(k - 1, n):
            if i - k + 1 > last_end:
                sub = s[i - k + 1 : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
                    continue
            
            if i - k > last_end:
                sub = s[i - k : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
                    
        return ans