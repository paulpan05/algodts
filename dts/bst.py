from __future__ import annotations

class BSTNode:
  def __init__(self, value: int, left: BSTNode = None, right: BSTNode = None):
    self.value = value
    self.left = left
    self.right = right