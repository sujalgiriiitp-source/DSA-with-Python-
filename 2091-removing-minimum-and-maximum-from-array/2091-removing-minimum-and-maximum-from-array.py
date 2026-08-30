class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        if min_index > max_index:
          min_index, max_index = max_index, min_index

        front_front = max_index + 1
        front_back = n - min_index
        both_sides = min_index + 1 + n - max_index

        return min(front_front, front_back, both_sides)

        