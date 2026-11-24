# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        second_part = slow.next
        prev = slow.next = None
        while second_part:
            temp = second_part.next
            second_part.next = prev
            prev = second_part
            second_part = temp
        
        first_part, second_part = head, prev

        while second_part:
            temp1, temp2 = first_part.next, second_part.next
            first_part.next = second_part
            second_part.next = temp1
            first_part, second_part = temp1, temp2