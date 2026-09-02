# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        positions = []
        curr = head
        while curr:
            dummy = ListNode()
            dummy.next = curr
            positions.append(dummy)
            curr = curr.next
        
        mid = len(positions) // 2

        first = positions[:mid]
        first.reverse()            
        second = positions[mid:]

        new_positions = []
        while first or second:
            if first:
                new_positions.append(first.pop())
            if second:
                new_positions.append(second.pop())

        for i in range(1, len(new_positions)):
            new_positions[i-1].next.next = new_positions[i].next

        new_positions[-1].next.next = None