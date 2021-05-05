class Node:
    def __init__(self, value, prev = None, next = None):
       self.value = value
       self.prev = prev
       self.next = next

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False
    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False
    def __gt__(self, other):
        if self.value > other.value:
            return True
        return False

class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
        self.length = 0

    def add(self, value):
        if self.lastNode is None:
            newNode = Node(value)
            #remove for non-cyclic linked list
            newNode.prev = newNode
            newNode.next = newNode

            self.head = newNode
            self.lastNode = newNode
            self.length += 1
            return newNode
        else:
            newNode = Node(value, self.lastNode)
            # remove for non-cyclic linked list
            newNode.next = self.head

            self.lastNode.next = newNode
            self.lastNode = newNode
            self.head.prev = self.lastNode
            self.length += 1
            return newNode

    def insert(self, node, value):
        if node.next is None:
            self.add(value)
        else:
            newNode = Node(value, node, node.next)
            node.next.prev = newNode
            node.next = newNode
            return newNode

    def insertLeft(self, node, value):
        newNode = Node(value, node.prev, node)
        node.prev.next = newNode
        node.prev = newNode
        return newNode

    def remove(self, node):
        if node != self.head:
            node.prev.next = node.next
        if node != self.lastNode:
            node.next.prev = node.prev
        del node

    def ithNode(self, index):
        if index >= self.length:
            raise IndexError("linked list index out of range")
        else:
            node = self.head
            for i in range(index):
                node = node.next
            return node

    def index(self, element):
        for i, value in enumerate(self):
            if value == element:
                return i
        else:
            raise ValueError(f"{element} is not in linked list")

    def __iter__(self):
        node = self.head
        while True:
            yield node.value
            node = node.next
            if node == self.lastNode:
                yield node.value
                break

    def __reversed__(self):
        node = self.lastNode
        while True:
            yield node.value
            node = node.prev
            if node == self.head:
                yield node.value
                break

    def __repr__(self):
        result = []
        for value in self:
            result.append(value)
        return " ".join(tuple(map(str, result)))

if __name__ == "__main__":
    lst = LinkedList()
    for i in range(5):
        lst.add(i)
    for index, value in enumerate(lst):
        print(f"{index}-th of the linked list is {value}")