from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        
        # Check if palindromic permutation is possible
        if sum(1 for f in count.values() if f % 2 != 0) > 1:
            return ""
            
        mid_char = next((c for c in "abcdefghijklmnopqrstuvwxyz" if count[c] % 2 != 0), "")
        half_freq = {c: f // 2 for c, f in count.items()}
            
        m = n // 2
        candidates = []
        current_prefix = []
        avail_freq = dict(half_freq)
        
        for L in range(m):
            # Branch 1: Diverge at current index L
            best_c = next((chr(c) for c in range(ord(target[L]) + 1, 123) if avail_freq.get(chr(c), 0) > 0), None)
            
            if best_c:
                temp_avail = dict(avail_freq)
                temp_avail[best_c] -= 1
                rest = "".join(chr(c) * temp_avail.get(chr(c), 0) for c in range(97, 123))
                left = "".join(current_prefix) + best_c + rest
                candidates.append(left + mid_char + left[::-1])
                
            # Branch 2: Match target[L]
            req_c = target[L]
            if avail_freq.get(req_c, 0) > 0:
                avail_freq[req_c] -= 1
                current_prefix.append(req_c)
            else:
                break
        else:
            # If we matched the entire left half exactly
            left = "".join(current_prefix)
            P = left + mid_char + left[::-1]
            if P > target:
                candidates.append(P)
                
        return min(candidates) if candidates else ""