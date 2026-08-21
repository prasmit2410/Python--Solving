# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Find the kth node of the current group
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                # Fewer than k nodes remain
                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse the current group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect the reversed group
            temp = group_prev.next
            group_prev.next = kth

            # Move to the next group
            group_prev = temp
        