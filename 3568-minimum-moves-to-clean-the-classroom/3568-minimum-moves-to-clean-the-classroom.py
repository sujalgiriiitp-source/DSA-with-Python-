from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        # Step 1: Map the grid and locate starting position and litter
        litter_pos = {}
        start_x = start_y = -1
        litter_count = 0
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_x, start_y = i, j
                elif classroom[i][j] == 'L':
                    litter_pos[(i, j)] = litter_count
                    litter_count += 1
                    
        target_mask = (1 << litter_count) - 1
        
        # Edge case: no litter to clean
        if target_mask == 0:
            return 0 
            
        # best_energy[x][y][mask] stores the max energy seen at a specific state to prune inefficient paths
        best_energy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        best_energy[start_x][start_y][0] = energy
        
        # queue stores: (x, y, current_mask, current_energy, moves)
        queue = deque([(start_x, start_y, 0, energy, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Step 2: BFS traversal
        while queue:
            x, y, mask, cur_e, moves = queue.popleft()
            
            # If all litter is collected, return the moves
            if mask == target_mask:
                return moves
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check boundaries and obstacles
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    
                    if cur_e == 0:
                        continue 
                        
                    nxt_e = cur_e - 1
                    nxt_mask = mask
                    cell = classroom[nx][ny]
                    
                    if cell == 'L':
                        nxt_mask |= (1 << litter_pos[(nx, ny)])
                    elif cell == 'R':
                        nxt_e = energy
                        
                    # Only proceed if we arrive at this state with MORE energy than we did previously
                    if nxt_e > best_energy[nx][ny][nxt_mask]:
                        best_energy[nx][ny][nxt_mask] = nxt_e
                        queue.append((nx, ny, nxt_mask, nxt_e, moves + 1))
                        
        return -1