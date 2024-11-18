from typing import List, Tuple, Optional

class MinHeap:
    """
    Implementation of a Min-Heap data structure to maintain a priority queue of elements.

    The heap stores tuples where the first element is used as the priority.
    """

    def __init__(self) -> None:
        """Initializes an empty heap."""
        self.heap: List[Tuple[int, any]] = []

    def push(self, item: Tuple[int, any]) -> None:
        """
        Inserts a new element into the heap.

        Args:
            item (Tuple[int, any]): The element to insert. The first value is treated as the priority.
        """
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> Optional[Tuple[int, any]]:
        """
        Removes and returns the element with the smallest priority.

        Returns:
            Optional[Tuple[int, any]]: The element with the smallest priority, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._sift_down(0)
        return min_item

    def _sift_up(self, index: int) -> None:
        """
        Reorganizes the heap after an insertion to maintain the min-heap property.

        Args:
            index (int): The index of the newly inserted element.
        """
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            # Swap the child with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index: int) -> None:
        """
        Reorganizes the heap after a removal to maintain the min-heap property.

        Args:
            index (int): The index of the root element to sift down.
        """
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Compare the current node with its left child
        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        # Compare the smallest node with the right child
        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child
        # Swap and continue sifting down if necessary
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

    def is_empty(self) -> bool:
        """
        Checks if the heap is empty.

        Returns:
            bool: True if the heap is empty, False otherwise.
        """
        return len(self.heap) == 0
