from linkedlist import linkedlist
import unittest
class linkedlist_test(unittest.TestCase):

    def test_list(self):
        list = linkedlist()
        list.insert(10,0)
        list.insert(20,0)
        list.insert(5,1)
        self.assertEqual(list.to_str(), '20 5 10')
        self.assertTrue(list.length() == 3)
        list.insert(15,3)
        node = list.findNodeAtPOS(1)
        self.assertTrue(node.data == 5)                
        print(list.to_str())

if __name__ == '__main__':
    unittest.main()
        



