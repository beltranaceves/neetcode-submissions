# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # O(n + m) time
        # O(n + m) space, optimal is O(1)

        # Base cases
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        if not list2 and not list2:
            return None

        curr = head = ListNode()
        head.next
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
            
        curr.next = list1 or list2
        return head.next
