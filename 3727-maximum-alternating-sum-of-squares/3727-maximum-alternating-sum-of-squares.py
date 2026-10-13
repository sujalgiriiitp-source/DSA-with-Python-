class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        squares = sorted(x * x for x in nums)
        
        n = len(squares)
        half = n // 2
        
       
        negative_sum = sum(squares[:half])
        
       
        positive_sum = sum(squares[half:])
        
        return positive_sum - negative_sum
        