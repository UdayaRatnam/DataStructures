class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
    def displayList(self):
        curr_val = self.head
        while curr_val is not None:
            print(curr_val.data)
            curr_val = curr_val.next
