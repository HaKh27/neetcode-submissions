"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map={None:None}

        current=head
        while current: 
            copy= Node(current.val)
            hash_map[current]=copy
            current=current.next
        
        current=head 
        while current: 
            copy=hash_map[current]
            copy.next= hash_map[current.next]
            copy.random= hash_map[current.random]
            current= current.next 
        

        return hash_map[head]
        