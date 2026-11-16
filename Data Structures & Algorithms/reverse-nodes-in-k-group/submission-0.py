# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        groupPrev= dummy

        while True:
            kth= self.getK(groupPrev,k)
            if not kth:
                break
        
            groupNext=kth.next
            #reverse group
            prev, current= kth.next, groupPrev.next 
            while current!=groupNext: 
                new_node= current.next 
                current.next=prev
                prev= current
                current= new_node 

            temp=groupPrev.next
            groupPrev.next= kth 
            groupPrev= temp

        return dummy.next
            



    def getK(self,curr,k):
        while curr and k>0: 
            curr=curr.next 
            k-=1
        return curr
        