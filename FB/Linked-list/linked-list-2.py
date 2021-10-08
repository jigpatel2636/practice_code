class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None # creating empty linked list since head is None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        n = self.head
        while n != None:
            print(n.data)
            n = n.ref

    def add_begin(self, data):
        new_node = Node(data)  # it creates node with reference as None ---> data|None
        new_node.ref = self.head
        self.head = new_node

    def add_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        n = self.head
        while n.ref != None:
            n = n.ref
        n.ref = new_node


    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)  # it creates node with reference as None ---> data|None
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            new_node = Node(data)
            n = self.head
            while n.ref.data != None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Nod is not found")
            else:
                new_node.ref = n.ref
                n.ref = new_node




LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_last(30)
LL1.add_last(40)
LL1.add_before(50,40)

LL1.print_LL()