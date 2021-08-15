# Double LinkedList

class Node:
    def __init__(self, data=None, prev=None, next=None):
        # arguments with default should be last
        self.prev = None
        self.data= data
        self.next = None

class DoubleLinkedList:
    def __init__(self, head=None):
        self.head = None

    def insertAtBeginning(self, Node):
        if self.head is None:
            self.head = Node
            self.head.prev = None
            self.head.next = None
        else:
            self.head.prev = Node
            Node.next = self.head
            self.head = Node
            Node.prev = None


    def insertAtEnd(self, Node):
        if self.head is None:
            self.insertAtBeginning(Node)
        else:
            itr = self.head
            while itr is not None:
                if itr.next is None:
                    itr.next = Node
                    Node.prev = itr
                    Node.next = None
                    break
                itr = itr.next

    def get_length(self):
        counter = 0
        if self.head is None:
            return counter
        else:
            itr = self.head
            while itr is not None:
                counter += 1
                itr = itr.next
            return counter

    def insertAt(self,index, Node):
        if index == 0:
            self.insertAtBeginning(Node)
        elif index == self.get_length()-1:
            self.insertAtEnd(Node)
        else:
            counter = 0
            itr = self.head
            while itr is not None:
                if counter == index:
                    temp = itr
                    prev_itr = temp.prev
                    prev_itr.next = Node
                    Node.prev = prev_itr
                    temp.prev = Node
                    Node.next = temp
                itr = itr.next
                counter += 1

    def removeAt(self, index):
        print(self.get_length())
        if index<0 or index>= self.get_length():
            raise Exception("index out of bounds")
        else:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None

            elif index == self.get_length()-1:
                itr = self.head
                while itr is not None:
                    if itr.next is None:
                        itr.prev.next = None
                        break
                    itr = itr.next

            else:
                counter = 0
                itr = self.head
                while itr is not None:
                    if counter == index:
                        temp = itr
                        prev_itr = temp.prev
                        next_itr = temp.next
                        prev_itr.next = next_itr
                        next_itr.prev = prev_itr
                        break
                    itr = itr.next
                    counter += 1


    def print_dblLinkedList(self):
        if self.head is None:
            print("Empty Double LinkedList")

        else:
            itr = self.head
            while itr is not None:
                print(itr.data, end="->")
                itr = itr.next



dblllist = DoubleLinkedList()
n1 = Node(10, None)
dblllist.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(30)
n2.next = n3
n3.prev = n2
n3.next = None

dblllist.print_dblLinkedList()
print("\n--------- insert at beginning 100-----------", end="\n")
dblllist.insertAtBeginning(Node(100))
dblllist.print_dblLinkedList()

print("\n--------- insert at end 1000-----------", end="\n")
dblllist.insertAtEnd(Node(1000))
dblllist.print_dblLinkedList()

print("\nLength: ", dblllist.get_length())

print("\n--------- remove index @ 2 -----------", end="\n")
dblllist.removeAt(2)
dblllist.print_dblLinkedList()

print("\n--------- insert at index @ 2 value 60-----------", end="\n")
dblllist.insertAt(2, Node(60))
dblllist.print_dblLinkedList()