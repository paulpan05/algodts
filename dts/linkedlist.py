from __future__ import annotations


class SNode:
    def __init__(self, value: object = None, nextNode: SNode = None):
        self.value = value
        self.next = nextNode


class DNode:
    def __init__(
        self, value: object = None, prevNode: DNode = None, nextNode: DNode = None
    ):
        self.value = value
        self.prev = prevNode
        self.next = nextNode
