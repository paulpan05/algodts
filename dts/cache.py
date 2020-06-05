from __future__ import annotations

from collections import OrderedDict
from typing import Dict, List


class LRUDNode:
    def __init__(
        self,
        key: int = None,
        prevNode: LRUDNode = None,
        nextNode: LRUDNode = None,
        value: int = None,
    ):
        self.key = key
        self.prev = prevNode
        self.next = nextNode
        self.value = value


class LRUCache:
    def __init__(self, capacity: int = 5):
        self._capacity = capacity
        self._size = 0
        self._head = LRUDNode()
        self._tail = LRUDNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._hmap: Dict[int, LRUDNode] = OrderedDict()

    def has_key(self, key: int) -> bool:
        return key in self._hmap

    def insert(self, key: int, value: str) -> bool:
        if self.has_key(key):
            return False
        tmp = LRUDNode(key, value=value)
        prev_front = self._head.next
        self._head.next = tmp
        prev_front.prev = tmp
        tmp.prev = self._head
        tmp.next = prev_front
        self._hmap[key] = tmp
        if self._size < self._capacity:
            self._size += 1
        else:
            evicted_key = self._tail.prev.key
            self._tail.prev.prev.next = self._tail
            self._tail.prev = self._tail.prev.prev
            self._hmap.pop(evicted_key)
        return True

    def get(self, key: int) -> str:
        if not self.has_key(key):
            raise ValueError("Key does not exist in cache.")
        cur = self._hmap[key]
        tmp_prev = cur.prev
        tmp_next = cur.next
        tmp_prev.next = tmp_next
        tmp_next.prev = tmp_prev
        cur.prev = self._head
        cur.next = self._head.next
        cur.prev.next = cur
        cur.next.prev = cur
        self._hmap[key] = self._hmap.pop(key)
        return cur.value

    def keys(self) -> List[int]:
        return list(reversed(self._hmap))

    def values(self) -> List[str]:
        values_list: List[str] = list()
        head = self._head
        while head.next is not None:
            values_list.append(head.value)
            head = head.next
        return values_list
