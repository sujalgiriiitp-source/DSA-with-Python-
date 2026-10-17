class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            return sum(int(d) for d in str(n))
        
        n = len(nums)
        
      
        arr = [(get_digit_sum(val), val, i) for i, val in enumerate(nums)]
        
       
        arr.sort(key=lambda x: (x[0], x[1]))
      
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
           
            if visited[i] or arr[i][2] == i:
                continue
            
          
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
            
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps