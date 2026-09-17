class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # dp[i] stores the minimum length of a valid subarray ending at or before index i
        dp = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_len = float('inf')
        ans = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window if current_sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            # Found a subarray ending at index `right` with sum equal to target
            if current_sum == target:
                curr_len = right - left + 1
                
                # Check if there is a valid non-overlapping subarray to the left
                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, curr_len + dp[left - 1])
                
                min_len = min(min_len, curr_len)
            
            # Maintain prefix minimum subarray length
            dp[right] = min_len
            
        return ans if ans != float('inf') else -1