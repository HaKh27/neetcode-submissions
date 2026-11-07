# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast= head 
        slow= head 

        while fast is not None and fast.next is not None: 
            slow= slow.next
            fast= fast.next.next 

        second= slow.next 
        slow.next= None 

        #prev and curr
        prev= None 
        current= second 

        #REVERSE THE SECOND HALF 
        while current is not None: 
            new_node= current.next
            current.next= prev 
            prev= current
            current= new_node

        second_head= prev 
        #merge sort
        p1= head
        p2= second_head 
        
        while p1 is not None and p2 is not None: 
            p1_temp= p1.next 
            p2_temp=p2.next 

            p1.next=p2 
            p2.next = p1_temp

            p1= p1_temp
            p2= p2_temp 

     




