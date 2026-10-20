class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Helper to check if a block nums[start : start+k] can be cyclically rotated into sorted order
        def is_valid_block(start: int, k: int) -> bool:
            drops = 0
            drop_idx = -1
            
            for j in range(k):
                curr = nums[start + j]
                nxt = nums[start + (j + 1) % k]
                if curr > nxt:
                    drops += 1
                    drop_idx = j
                    if drops > 1:
                        return False
            
            # If 0 drops, the block is already sorted
            if drops == 0:
                return True
            
            # If 1 drop, after rotation the new first element is at drop_idx + 1.
            # Check if elements spanning adjacent blocks stay globally non-decreasing.
            # (If this is not the last block, the largest element in this block must be <= smallest in next block)
            # Actually, standard sortability only requires checking block boundary conditions if needed, 
            # but comparing rotated block's minimum and maximum against sorted bounds ensures global order.
            return True

        # Pre-calculate sorted array or check globally
        s = sorted(nums)

        for k in range(1, n + 1):
            if n % k != 0:
                continue
            
            is_sortable = True
            for i in range(0, n, k):
                # 1. Quick check: multiset match against global sorted position
                # Using element sums or min/max bounds saves time
                block_a = nums[i:i + k]
                block_b = s[i:i + k]
                
                # Check if block_a can rotate into block_b
                # A block rotates to block_b iff sorted(block_a) == block_b and has <= 1 cyclic drop
                if sorted(block_a) != block_b:
                    is_sortable = False
                    break
                
                # Check for at most 1 cyclic drop
                drops = 0
                for j in range(k):
                    if block_a[j] > block_a[(j + 1) % k]:
                        drops += 1
                        if drops > 1:
                            break
                
                if drops > 1:
                    is_sortable = False
                    break
            
            if is_sortable:
                ans += k
                
        return ans