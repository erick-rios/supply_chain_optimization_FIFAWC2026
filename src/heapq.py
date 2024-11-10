# heapq.py
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        """Inserta un nuevo elemento en el heap."""
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Elimina y devuelve el elemento mínimo."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()  # Mover último elemento al inicio
        self._sift_down(0)
        return min_item

    def _sift_up(self, index):
        """Reorganiza el heap después de una inserción."""
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index):
        """Reorganiza el heap después de una eliminación."""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

    def is_empty(self):
        """Devuelve True si el heap está vacío."""
        return len(self.heap) == 0
