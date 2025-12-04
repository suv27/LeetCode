

class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
    

class linkedList:
    def __init__ (self, head=None):
        self.head = head
    
    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
    
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end=" -> ",)
            currentNode = currentNode.nextNode
        print("None")
            
    def getMiddleElement(self):
        slowRunner = self.head
        fastRunner = self.head
        tick = False

        while fastRunner:
            fastRunner = fastRunner.nextNode
            if tick:
                slowRunner = slowRunner.nextNode
            tick = not tick
        return print(slowRunner.value)


ll = linkedList()
ll.insert("1")
ll.insert("3")
ll.insert("5")
ll.insert("7")
ll.insert("9")
ll.insert("11")
ll.insert("13")
ll.printLinkedList()
ll.getMiddleElement()