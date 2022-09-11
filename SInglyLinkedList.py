class Node:
   def __init__(self,data=None,next=None):
      self.data = data
      self.next = next
   def setData(self,data):
      self.data = data
   def getData(self):
      return self.data
   def setNext(self,next):
      self.next = next
   def getNext(self):
      return self.next

class SinglyLinkedList():
   def __init__(self):
      self.head = None

   def insertBegin(self, data):
      if self.head == None:
         temp = Node(data)
         self.head = temp
      else:
         temp = Node(data)
         temp.next = self.head
         self.head = temp
   def insertEnd(self,data):
      temp = Node(data)
      current = self.head
      while(current.next != None):
         current = current.next
      current.next = temp

   def printList(self):
      temp = self.head
      while(temp):
         print(temp.data, end=" ")
         temp = temp.next



if __name__ == "__main__":

   test = SinglyLinkedList()
   test.head = Node(44)
   test.insertEnd(47)
   for i  in range(10):
      test.insertEnd(i)
   test.insertBegin("test")
   test.printList()




