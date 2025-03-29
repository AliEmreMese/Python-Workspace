class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(data)
        elif index == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def erase(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        if index == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            for _ in range(index):
                current = current.next
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
        self.size -= 1

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def access(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def get(self):
        return self.size

    def traversal(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display(self):
        current = self.head
        while current:
            print(f"[{current.data}]", end=" <-> " if current.next else "\n")
            current = current.next

dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("D")
dll.prepend("Start")
dll.insert(2, "C")

print("Liste:")
dll.display()

print("Eleman 'B' indeksinde:", dll.search("B"))

print("2. indeks:", dll.access(2))

dll.erase(0)
print("Baş eleman silindi:")
dll.display()

print("Liste uzunluğu:", dll.get())

print("Tüm elemanlar:", dll.traversal())
