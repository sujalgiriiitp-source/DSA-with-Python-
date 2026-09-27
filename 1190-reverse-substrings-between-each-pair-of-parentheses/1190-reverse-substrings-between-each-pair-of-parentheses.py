class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair = {}
        stack = []
        
        # Step 1: Record the matching pairs of parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        res = []
        i, direction = 0, 1
        
        # Step 2: Traverse string. Teleport at brackets and reverse direction.
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction
            
        return "".join(res)
        