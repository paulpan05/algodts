import unittest
from dts import LRUCache

class TestLRUCache(unittest.TestCase):

  def test_insertion(self):
    lrucache = LRUCache()
    lrucache.insert(5, 'hello')
    lrucache.insert(4, 'world')
    lrucache.insert(10, 'how are you')
    lrucache.insert(1, 'paul')
    lrucache.insert(2, 'asdf')
    lrucache.insert(3, 'jkl;')
    print(lrucache.keys())

if __name__ == '__main__':
  unittest.main()