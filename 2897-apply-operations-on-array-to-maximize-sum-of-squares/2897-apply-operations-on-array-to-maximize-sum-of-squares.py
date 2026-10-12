class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit_counts[i] += 1
                    
        total_sum = 0
        
        for _ in range(k):
            current_val = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_val |= (1 << i)
                    bit_counts[i] -= 1
                    
            total_sum = (total_sum + current_val * current_val) % MOD
            
        return total_sum
        