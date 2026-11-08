# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return 

        dummy= ListNode(0,head)
        slow=dummy
        fast=dummy 

        for _ in range(n):
            if fast is None: 
                return
            fast=fast.next
        
        while fast.next is not None:
            slow= slow.next
            fast= fast.next 
        
        slow.next= slow.next.next
        
        return dummy.next


        