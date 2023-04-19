class SSLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

# 1
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def clear(self):
        self.head = None
        self.size = 0

  #2
class SinglyLinkedList:


    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return data
            current = current.next
        return False

#3

def insert(self, prev_data, data):
    new_node = SSLNode
    current = self.data
    while current is not None:
        if current.data == prev_data:
            new_node.next = current.next
            current.next = new_node
            self.size += 1
            return True
        current = current.next
    return False

#4
def delete_node(self, data):
    if self.head is None:
        return
    if self.head.data == data:
        self.head == self.head.next
        self.size -= 1
        return
    current = self.head
    while current.next is not None:
        if current.next.data == data:
            current.next = current.next.next
            self.size -= 1
            return
        current = current.next


# 5

class DLLNode:
    def __init__(self, value):
        self.previous = None
        self.data = value
        self.next = None


class DLLNode:
    def __init__(self):
        self.head = None

