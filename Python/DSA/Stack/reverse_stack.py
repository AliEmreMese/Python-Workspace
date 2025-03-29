class Reverse_Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop(0)
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty.Cannot pop.")
            return None
        
    def peek(self):
        if not self.is_empty():
            top_item = self.items[0]
            print(f"Peek: {top_item}")
            return top_item
        else:
           print("Stack is empty.Cannot peek.")
           return None
        
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items: ", self.items)