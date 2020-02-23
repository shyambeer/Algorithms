class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next=self.head
        self.head = node

    def printl(self):
        current  = self.head
        while current:
            print (current.data)
            current= current.next

    def removeDups(self):
        currentNode = self.head
        while currentNode and currentNode.next:
            if currentNode.data == currentNode.next.data:
                currentNode.next = currentNode.next.next
                continue
            currentNode = currentNode.next
        return self.head



l= LinkedList()
l.insert(3)
l.insert(3)
l.insert(2)
l.insert(1)
l.insert(1)


l.printl()
print ("===============")

l.removeDups()
l.printl()