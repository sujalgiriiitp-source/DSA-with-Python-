class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack, seen, res = [expression], {expression}, set()
        
        while stack:
            exp = stack.pop()
            if '{' not in exp:
                res.add(exp)
                continue
                
            r = exp.find('}')
            l = exp.rfind('{', 0, r)
            
            before, after = exp[:l], exp[r+1:]
            for part in exp[l+1:r].split(','):
                new_exp = before + part + after
                if new_exp not in seen:
                    seen.add(new_exp)
                    stack.append(new_exp)
                    
        return sorted(list(res))