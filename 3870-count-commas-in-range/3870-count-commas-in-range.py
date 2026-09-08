class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000
        
        while n >= threshold:
            # Add commas for all numbers >= current threshold
            total_commas += (n - threshold + 1)
            # Move to the next threshold (1,000,000 -> 1,000,000,000, etc.)
            threshold *= 1000
            
        return total_commas