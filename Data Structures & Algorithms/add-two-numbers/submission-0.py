# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        #Initialize carry var
        carry=0 
        #loop as long as l1,l2, or carry exists
        while l1 or l2 or carry:
            #store l1.val in a var and make it 0 if l1.val doesn't exist
            val1=l1.val if l1 else 0
            #store l2.val or make it 0 if it doesnt exist 
            val2= l2.val if l2 else 0 

            #add everything + carry 
            val= val1+val2+carry 
            #if the sum is greater than 10, update carry 
            carry=val//10 
            #hold on to the leftover value 
            val=val%10 

            #store the value in a new node
            current.next= ListNode(val)
            
            #update pointers
            current=current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next 
            



        