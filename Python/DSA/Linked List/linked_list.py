class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR! 'Get' index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR! 'Erase' index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


my_list =  Linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

your_list = Linked_list()

your_list.append(2)
your_list.append(5)


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)

print(a.data)