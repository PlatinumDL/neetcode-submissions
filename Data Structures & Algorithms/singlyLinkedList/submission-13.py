class LinkedList:

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next
    
    def __init__(self, head=None, tail=None):
        self.head = LinkedList.Node(None,None)
        self.tail = LinkedList.Node(None,None)
    
    def get(self, index: int) -> int:
        cur = self.head
        if cur.val is None:
            return -1

        for i in range(index):
            if cur.next == None:
                return -1
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        new_node = LinkedList.Node(val,self.head)
        if self.head.val is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = LinkedList.Node(val, None)
        if self.tail.val is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head.val is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        cur = self.head
        for i in range(index - 1):
            if cur.next is None or cur.next.val is None:
                return False
            cur = cur.next

        if cur.next is None or cur.next.val is None:
            return False

        if cur.next.next is None:               # removing tail
            cur.next = None
            self.tail = cur
        else:
            cur.next = cur.next.next

        return True


    def getValues(self) -> List[int]:
        toPrint = []
        cur = self.head
        while cur is not None and cur.val is not None:
            toPrint.append(cur.val)
            cur = cur.next
        return(toPrint)

        
