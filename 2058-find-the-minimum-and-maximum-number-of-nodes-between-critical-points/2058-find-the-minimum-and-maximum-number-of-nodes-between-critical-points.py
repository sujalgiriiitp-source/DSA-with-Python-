# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Minimum 3 nodes are needed to form any critical point
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        idx = 2
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        while curr and curr.next:
            # Check if current node is a local maxima or local minima
            is_maxima = (curr.val > prev.val) and (curr.val > curr.next.val)
            is_minima = (curr.val < prev.val) and (curr.val < curr.next.val)
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = idx
                else:
                    min_dist = min(min_dist, idx - prev_cp)
                
                prev_cp = idx
            
            prev = curr
            curr = curr.next
            idx += 1
            
        # Less than 2 critical points found
        if min_dist == float('inf'):
            return [-1, -1]
        
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]