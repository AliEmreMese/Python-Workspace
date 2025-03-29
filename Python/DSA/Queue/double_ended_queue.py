class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.append(item)
        print(f"Added to front: {item}")

    def add_rear(self, item):
        self.items.insert(0, item)
        print(f"Added to rear: {item}")

    def remove_front(self):
        if not self.is_empty():
            removed_item = self.items.pop()
            print(f"Removed from front: {removed_item}")
            return removed_item
        else:
            print("Reverse Deque is empty. Cannot remove from front.")
            return None

    def remove_rear(self):
        if not self.is_empty():
            removed_item = self.items.pop(0)
            print(f"Removed from rear: {removed_item}")
            return removed_item
        else:
            print("Reverse Deque is empty. Cannot remove from rear.")
            return None

    def peek_front(self):
        if not self.is_empty():
            front_item = self.items[-1]
            print(f"Peek front: {front_item}")
            return front_item
        else:
            print("Reverse Deque is empty. Cannot peek front.")
            return None

    def peek_rear(self):
        if not self.is_empty():
            rear_item = self.items[0]
            print(f"Peek rear: {rear_item}")
            return rear_item
        else:
            print("Reverse Deque is empty. Cannot peek rear.")
            return None

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Reverse Deque is empty.")
        else:
            print("Reverse Deque items:", self.items)