class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, i: int) -> int:
        curr = self.head
        idx = 0
        while curr:
            if idx == i:
                return curr.val
            curr = curr.next
            idx += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, i: int) -> bool:
        if not self.head:
            return False
        if i == 0:
            self.head = self.head.next
            return True
        curr = self.head
        idx = 0
        while curr and idx < i - 1:
            curr = curr.next
            idx += 1
        if not curr or not curr.next:
            return False
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr