import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        ans = math.comb(n + k - 1, 2 * k)

        return ans % MOD
        