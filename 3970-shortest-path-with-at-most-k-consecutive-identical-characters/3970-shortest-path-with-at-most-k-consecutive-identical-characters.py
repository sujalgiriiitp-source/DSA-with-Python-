import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[node][count] stores the minimum cost to reach 'node' with 'count' consecutive identical characters
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        
        pq = [(0, 0, 1)]
        
        while pq:
            cost, u, count = heapq.heappop(pq)
            
            # If we found a shorter path to this exact state already, skip it
            if cost > dist[u][count]:
                continue
                
         
            if u == n - 1:
                return cost
                
            # Explore neighbors
            for v, w in adj[u]:
                
                nxt_count = count + 1 if labels[u] == labels[v] else 1
                
               
                if nxt_count <= k:
                    nxt_cost = cost + w
                    
                   
                    if nxt_cost < dist[v][nxt_count]:
                        dist[v][nxt_count] = nxt_cost
                        heapq.heappush(pq, (nxt_cost, v, nxt_count))
                        
        return -1
        