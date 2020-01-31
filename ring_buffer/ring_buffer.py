from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

# ring buffer, i.e., circular queue
# oldest item is overwritten by newest when buffer is full

    def append(self, item):
        # self.current is new item
        if self.current is None:
            self.current = self.storage.head

        # but if the buffer is full, then ~~>
        if self.storage.length == self.capacity:
            self.current.value = item
            self.current = self.current.next

        # otherwise add new item to the tail of the queue
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
