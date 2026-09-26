class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_dict = {k: v for k, v in knowledge}
        ans = []
        cur_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                key = "".join(cur_key)
                ans.append(knowledge_dict.get(key, "?"))
                cur_key = []
                in_bracket = False
            else:
                if in_bracket:
                    cur_key.append(char)
                else:
                    ans.append(char)
                    
        return "".join(ans)
        