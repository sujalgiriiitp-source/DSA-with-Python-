class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000
        
        # Keep checking powers of 1000
        while n >= threshold:
            # Add the number of integers that have a comma at this position
            total_commas += (n - threshold + 1)
            threshold *= 1000
            
        return total_commas
        