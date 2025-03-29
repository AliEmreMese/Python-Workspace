class Reverse_Deque:
    def __init__(self):
        self.items = []  # Deque öğelerini depolamak için boş bir liste

    def add_front(self, item):
        """Öğeyi deque'nin önüne ekle."""
        self.items.insert(0, item)  # Öğeyi listenin en başına ekle
        print(f"Added to front: {item}")

    def add_rear(self, item):
        """Öğeyi deque'nin arkasına ekle."""
        self.items.append(item)  # Öğeyi listenin sonuna ekle
        print(f"Added to rear: {item}")

    def remove_front(self):
        """Deque'den en öndeki öğeyi çıkar ve döndür."""
        if not self.is_empty():
            removed_item = self.items.pop(0)  # En öndeki öğeyi çıkar
            print(f"Removed from front: {removed_item}")
            return removed_item
        else:
            print("Deque is empty. Cannot remove from front.")
            return None

    def remove_rear(self):
        """Deque'den en arka öğeyi çıkar ve döndür."""
        if not self.is_empty():
            removed_item = self.items.pop()  # En arka öğeyi çıkar
            print(f"Removed from rear: {removed_item}")
            return removed_item
        else:
            print("Deque is empty. Cannot remove from rear.")
            return None

    def peek_front(self):
        """Deque'nin en öndeki öğesini döndür, çıkarma işlemi yapmaz."""
        if not self.is_empty():
            front_item = self.items[0]  # En öndeki öğe
            print(f"Peek front: {front_item}")
            return front_item
        else:
            print("Deque is empty. Cannot peek front.")
            return None

    def peek_rear(self):
        """Deque'nin en arka öğesini döndür, çıkarma işlemi yapmaz."""
        if not self.is_empty():
            rear_item = self.items[-1]  # En arka öğe
            print(f"Peek rear: {rear_item}")
            return rear_item
        else:
            print("Deque is empty. Cannot peek rear.")
            return None

    def is_empty(self):
        """Deque'nin boş olup olmadığını kontrol et."""
        return len(self.items) == 0

    def size(self):
        """Deque'deki öğe sayısını döndür."""
        return len(self.items)

    def display(self):
        """Deque'deki tüm öğeleri göster."""
        if self.is_empty():
            print("Deque is empty.")
        else:
            print("Deque items:", self.items)