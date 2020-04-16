from __future__ import annotations

class SNode:
  def __init__(self, value: int = None, nextNode: SNode = None):
    self.value = value
    self.next = nextNode

class DNode(SNode):
  def __init__(self, value: int = None, prevNode: DNode = None, nextNode: DNode = None):
    super.__init__(value, nextNode)
    self.prev = prevNode