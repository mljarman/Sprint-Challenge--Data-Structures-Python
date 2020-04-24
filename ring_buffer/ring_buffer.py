from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #self.current = self.storage.head
        # if at less than capacity, add item to tail:
        if self.storage.length < self.capacity:
            # current is the head
            self.current = self.storage.head
            self.storage.add_to_tail(item)
        # if at capacity, need to overwrite oldest item value
        # with new item value
        else:
            # item to add becomes current
            self.current.value = item
            # if it's not at the end, will replace next item
            if self.current.next is not None:
                self.current = self.current.next
            else:
                self.current = self.storage.head



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # start at beginning:
        current_node = self.storage.head
        # if head not none:
        if current_node is not None:
            # add the first node's value to the array
            list_buffer_contents.append(current_node.value)
            # for each node that's not None, add its value to the array.
            while current_node.next is not None:
                current_node = current_node.next
                list_buffer_contents.append(current_node.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
