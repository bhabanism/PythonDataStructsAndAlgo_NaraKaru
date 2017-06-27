class linkedlist:
    head = None
    class node:
        data = None
        next = None
        def __init__(self, data):
            self.data = data
            self.Next = None

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

    
    def __insertAtBeginning(self, data):
        newnode = self.node(data)
        newnode.data = data

        if self.length() == 0:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def __insertAtEnd(self, data):
        newnode = self.node(data)
        current = self.head

        while current.next != None:
            current = current.next

        current.next = newnode

    def __insertAtPOS(self, data, pos):
        newnode = self.node(data)
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
            self.__insertAtBeginning(data)
        elif pos == self.length():
            self.__insertAtEnd(data)
        else:
            self.__insertAtPOS(data, pos)

    def findNodeAtPOS(self, pos):
        if pos >= self.length() or pos < 0:
            return None
        
        count = 0
        current = self.head
        while count < pos-1:
            count += 1
            current = current.next

        return current.next

    def __deleteFromBeginning(self):
        if self.length() == 0:
            raise ValueError('Nothing to delete, list empty')
        else:
            self.head = self.head.next

    def __deleteFromEnd(self):
        if self.length() == 0:
            raise ValueError('Nothing to delete, list empty')
        else:
            current = self.head

            while current.next != None:
                previous = current
                current = current.next

            previous.next = None

    def deleteNode(self, node):
        if self.length() == 0:
            raise ValueError('Nothing to delete, list empty')
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError('Node not in list')
                else:
                    previous = current
                    current = current.next

            if previous is None:
                # head matches the node
                self.head = current.next
            else:
                previous.next = current.next

    def deleteNodeByValue(self, value):
        current = self.head
        previous = self.head
        while current.next != None or current.data != value:
            if current.data == value:
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next

        raise ValueError('Value not present in list')


    def deleteAtPOS(self, pos):
        if pos == 0:
           self.__deleteFromBeginning()
           return
        elif pos == self.length():
           self.__deleteFromEnd()
           return

        count = 0
        current = self.head
        previous = self.head

        if pos > self.length() or pos < 0:
            raise ValueError('Invalid position ' + str(pos))
        else:
            while current.next != None or count < pos:
                print("count " + str(count))
                print("pos "  + str(pos))
                
                if count == pos:
                    print("deleting " + str(current.data))
                    previous.next = current.next
                    return
                else:
                    count += 1
                    previous = current
                    current = current.next




    

    



