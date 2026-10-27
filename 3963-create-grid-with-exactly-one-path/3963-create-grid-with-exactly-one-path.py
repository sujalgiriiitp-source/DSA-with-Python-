class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        
        # First row: all free cells ('.')
        grid.append('.' * n)
        
        # Subsequent rows: block everything except the last column
        for _ in range(m - 1):
            grid.append('#' * (n - 1) + '.')
            
        return grid