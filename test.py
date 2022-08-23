from SLinkedList import Node,SLinkedList




if __name__ == "__main__":
    groceries = SLinkedList()
    groceries.head = Node("eggs")
    l1 = Node("milk")
    l2 = Node("fruit")
    l3 = Node("creamer")
    groceries.head.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = Node("granola")
    groceries.displayList()
