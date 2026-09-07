class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        end = [0] * 26
        total = 0

        for c in s:
            idx = ord(c) - ord('a')



            added = (total + 1 - end[idx]) % MOD

            end[idx] = (end[idx] + added) % MOD
            total = (total + added) % MOD

        return total