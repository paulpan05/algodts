import unittest
from dts import BSTNode

class TestBST(unittest.TestCase):

  def test_insertion(self):
    node1 = BSTNode(5)
    node2 = BSTNode(4, right = node1)
    self.assertEqual(node2.right, node1)

if __name__ == '__main__':
  unittest.main()