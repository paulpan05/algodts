from __future__ import annotations
import json

class BSTNode:
  def __init__(self, value: int, left: BSTNode = None, right: BSTNode = None):
    self.value = value
    self.left = left
    self.right = right

class BST:
  def __init__(self, root: BSTNode = None):
    self.root = root
  def insert(self, value: int) -> None:
    if not self.root:
      self.root = BSTNode(value)
    else:
      cur_node = self.root
      prev_node = None
      while cur_node != None:
        if value < cur_node.value:
          prev_node = cur_node
          cur_node = cur_node.left
        elif value > cur_node.value:
          prev_node = cur_node
          cur_node = cur_node.right
        else:
          raise ValueError('Value already exists in tree')
      if value < prev_node.value:
        prev_node.left = BSTNode(value)
      else:
        prev_node.right = BSTNode(value)
  def has_value(self, value: int) -> bool:
    cur_node = self.root
    while cur_node != None:
      if value < cur_node.value:
        cur_node = cur_node.left
      elif value > cur_node.value:
        cur_node = cur_node.right
      else:
        return True
    return False
  def __str__(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)