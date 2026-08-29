class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        if n<= 1:
            return nums

        indexed_nums = sorted([(nums[i], i) for i in range(n)])

        res =[0] * n
        i = 0

        while i < n:
            j = i + 1

            while j < n and indexed_nums[j][0] - indexed_nums[j-1][0]<= limit:
                j += 1 

            component_indices = sorted([indexed_nums[k][1] for k in range(i, j)])

            for k in range(len(component_indices)):
                res[component_indices[k]] = indexed_nums[i + k] [0]
            
            i = j

        return res
        