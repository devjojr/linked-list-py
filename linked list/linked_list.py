class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self, head):
        self.head = head

    def __len__(self):
        length = 0
        current = self.head

        while current is not None:
            length += 1
            current = current.next
        return length

    def insert(self, data):
        if data is None:
            return None

        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return None

        node = Node(data)

        if self.head is None:
            self.head = node
            return node
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = node
        return node

    def find(self, data):
        if data is None:
            return None

        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        if self.head is None:
            return None
        if data is None:
            return
        if self.head.data == data:
            self.head = None
            return

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next
        return None

    def get_all_data(self):
        if self.head is None:
            return None

        result = []
        current = self.head

        while current is not None:
            result.append(str(current.data))
            current = current.next
        return ' => '.join(result)

    def print_list(self):
        if self.head is None:
            return None

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next
