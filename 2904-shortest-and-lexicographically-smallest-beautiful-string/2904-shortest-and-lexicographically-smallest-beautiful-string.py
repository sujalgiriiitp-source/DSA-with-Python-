class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""
        
        for right in range(len(s)):
            if s[right] == '1':
                ones += 1
            
            while ones == k:
                sub = s[left:right +1]

                if not ans:
                    ans = sub
                elif len(sub) < len(ans):
                    ans = sub
                elif len(sub) == len(ans):
                    ans = min(ans, sub)

                if s [left ] == '1':
                    ones -= 1
                left += 1

        return ans