from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: object
    next: Node or None

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


class LinkedList:
    head = None
    tail = None
    __current = None
    size = 0

    def append(self, obj):
        node = Node(obj, None)
        if self.head is None:
            self.head = node
            self.tail = node
            self.__current = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def find(self, obj):
        node = self.head

        for node in self:
            if node.value == obj:
                return node

        return None

    def __find_next(self, obj):
        node = self.head

        for node in self:
            if node.next is None:
                break

            if node.next.value == obj:
                return node

        return None

    def remove(self, obj):
        node = self.__find_next(obj)

        if node is None:
            return -1

        if node.next.next is None:
            self.tail = node
        else:
            node.next = node.next.next

        self.size -= 1

        return 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.__current
        if current is None:
            self.__current = self.head
            raise StopIteration

        self.__current = self.__current.next
        return current

    def __str__(self):
        for node in self:
            print(node)
