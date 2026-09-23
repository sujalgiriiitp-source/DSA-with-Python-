class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        # If the total sum is exactly x, we must remove all elements
        if target == 0:
            return len(nums)
            
        # If x is greater than the sum of all elements, it's impossible
        if target < 0:
            return -1
            
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window to find the maximum subarray with sum == target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left if the sum exceeds our target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we find a valid window, update the maximum length
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # The minimum operations will be the total length minus the max subarray length
        return len(nums) - max_len if max_len != -1 else -1
        