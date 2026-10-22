class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        # Helper to check if array is cyclically increasing
        def is_cyclically_increasing(arr):
            count = 0
            for i in range(n):
                if arr[i] > arr[(i + 1) % n]:
                    count += 1
            return count <= 1

        # Check forward and reversed configurations
        rev_nums = nums[::-1]
        inc_forward = is_cyclically_increasing(nums)
        inc_reverse = is_cyclically_increasing(rev_nums)

        if not inc_forward and not inc_reverse:
            return -1

        # Run BFS to find shortest path from (type=0, shift=0) to sorted target
        # State: (type, shift)
        # type 0: rotated nums
        # type 1: rotated rev_nums
        
        from collections import deque
        
        # Target index of 0 in forward array
        idx_zero_f = nums.index(0)
        # Target index of 0 in reversed array
        idx_zero_r = rev_nums.index(0)

        # Candidates for minimum steps
        ans = float('inf')

        # Mode 1: Pure forward rotations (if cyclically increasing)
        if inc_forward:
            # Standard left rotations to bring 0 to the front
            rotations = idx_zero_f
            ans = min(ans, rotations)
            
            # Reverse -> Right Rotations -> Reverse
            # (1 reverse + (n - idx_zero_f) % n rotations + 1 reverse)
            rotations_via_rev = 1 + ((n - idx_zero_f) % n) + 1
            ans = min(ans, rotations_via_rev)

        # Mode 2: Reversed array rotations (if cyclically decreasing originally)
        if inc_reverse:
            # 1 Reverse to make it increasing + left rotations
            rot_rev_1 = 1 + idx_zero_r
            ans = min(ans, rot_rev_1)

            # Rotate first, then reverse
            rot_rev_2 = ((n - idx_zero_r) % n) + 1
            ans = min(ans, rot_rev_2)

        return ans if ans != float('inf') else -1
        