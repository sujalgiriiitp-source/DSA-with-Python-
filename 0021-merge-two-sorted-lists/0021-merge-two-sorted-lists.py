# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        c = d

        while list1 and list2:

             if list1.val > list2.val:
                 c.next = list2
                 c = list2
                 list2 = list2.next
             else:
                c.next = list1
                c = list1
                list1 = list1.next
        if list1:
                c.next = list1
        else:
                c.next = list2
        
        return d.next