import unittest
from dts import BSTNode, BST

class TestBST(unittest.TestCase):

  def test_insertion(self):
    bst = BST()
    bst.insert(0)
    bst.insert(-1)
    bst.insert(1)
    bst.insert(-2)
    print(str(bst))

if __name__ == '__main__':
  unittest.main()