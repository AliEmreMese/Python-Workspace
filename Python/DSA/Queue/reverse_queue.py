class Reverse_Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.items.pop(0)
            print(f"Dequeued: {dequeued_item}")
            return dequeued_item
        else:
            print("Queue is empty. Cannot dequeue.")
            return None
        
    def peek(self):
        if not self.is_empty():
            front_item = self.items[0]
            print(f"Peek: {front_item}")
            return front_item
        else:
            print("Queue is empty. Cannot peek.")
            return None
        
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue items: ", self.items)