from node import node
class linkedlist:
    head = None
    def __init__(self):
        self.head = None

    def length(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next

        return count

    def to_str(self):
        s = ''
        current = self.head
        while current !=None:
            s += str(current.data) + ' '
            current = current.next

        return s.strip()

    
    def insertAtBeginning(self, data):
        newnode = node(data)
        newnode.data = data

        if self.length() == 0:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insertAtEnd(self, data):
        newnode = node(data)
        current = self.head

        while current.next != None:
            current = current.next

        current.next = newnode

    def insertAtPOS(self, data, pos):
        newnode = node(data)
        count = 0
        current = self.head
        while count < pos-1:
            count += 1
            current = current.next
        
        newnode.next = current.next
        current.next = newnode
        

    def insert(self, data, pos):
        if pos > self.length() or pos < 0:
            return None
        
        if pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.length():
            self.insertAtEnd(data)
        else:
            self.insertAtPOS(data, pos)

    def deleteFromBeginning(self):
        if self.length() == 0:
            raise ValueError('Nothing to delete, list empty')
        else:
            self.head = self.head.next

    def deleteFromEnd(self):
        if self.length() == 0:
            raise ValueError('Nothing to delete, list empty')
        else:
            current = self.head

            while current.next != None:
                previous = current
                current = current.next

            previous.next = None


    def



