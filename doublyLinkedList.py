class Node:
    def __init__(self,data,next=None,prev=None):
        self.data= data
        self.next = next
        self.prev = prev
class DLL:
    def __init__(self):
        self.head = None
        self.tail =  None

    def pushHead(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pushTail(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            curr = self.head 
            while curr.next:
                curr=curr.next
            curr.next= newNode
            self.tail = newNode
            
    def printDLL(self):
        curr = self.head 
        while curr is not self.tail:
            print(curr.data)
            curr=curr.next
        print(curr.data)


instance=DLL()
instance.pushHead(2)
instance.pushHead(3)
instance.pushHead(4)
instance.pushHead(5)
instance.pushHead(62)
instance.pushTail(666)
instance.pushTail(11)
instance.pushTail(344)
instance.printDLL()
