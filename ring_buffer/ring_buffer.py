from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current is None:
            # if append is called and the current ringbuffer is empty
            # then current is first item in storage
            self.current = self.storage.head

        if self.storage.length == self.capacity:
            # if the contents of storage reach the set capacity
            # then the current value is set to item
            # and current becomes the next oldest item
            self.current.value = item
            self.current = self.current.next

        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
