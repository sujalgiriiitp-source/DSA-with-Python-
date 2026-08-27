from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        best_ans = ""
        prefix = ""
        
        # We will iterate through the alphabet to find the smallest valid character
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(len(target)):
            t_char = target[i]
            diverge_char = None
            
            # 1. Try to find the smallest available character strictly greater than target[i]
            for c in alphabet:
                if c > t_char and freq[c] > 0:
                    diverge_char = c
                    break
            
            # If we found a character to diverge, build the candidate
            if diverge_char:
                # Temporarily use this character
                freq[diverge_char] -= 1
                
                # The rest of the string should be the remaining characters sorted
                rem_chars = []
                for c in alphabet:
                    rem_chars.append(c * freq[c])
                    
                candidate = prefix + diverge_char + "".join(rem_chars)
                best_ans = candidate # Overwrites with a better (longer prefix) candidate
                
                # Backtrack to try matching the target exactly instead
                freq[diverge_char] += 1
                
            # 2. Try to match the target character to extend the exact prefix
            if freq[t_char] > 0:
                prefix += t_char
                freq[t_char] -= 1
            else:
                # If we cannot match target[i], we can't extend the prefix further.
                break
                
        return best_ans