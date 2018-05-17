class listNode:
    def __init__(self, value):
	    self.value = value
	    self.next = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

class linkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, value):
        newhead = listNode(value)
        newhead.setNext(self.head)
        self.head = newhead

    def pop(self, value):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getValue() == value:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            current = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, value):
        current = self.head
        found = False

        while current != None and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        return found
