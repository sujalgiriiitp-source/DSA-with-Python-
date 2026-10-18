import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def count_ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            l_len, r_len = len(left), len(right)
            
            # Number of ways to interleave left and right elements
            comb = math.comb(l_len + r_len, l_len) % MOD
            
            return (comb * count_ways(left) % MOD * count_ways(right)) % MOD

        return (count_ways(nums) - 1) % MOD
        