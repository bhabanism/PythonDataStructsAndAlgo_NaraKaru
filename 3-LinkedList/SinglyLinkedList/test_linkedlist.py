from linkedlist import linkedlist
import unittest
class linkedlist_test(unittest.TestCase):

    def test_list_insert_beginning(self):
        list = linkedlist()
        list.insert(10,0)
        list.insert(20,0)
        list.insert(5,1)
        self.assertEqual(list.to_str(), '20 5 10')
        self.assertTrue(list.length() == 3)


if __name__ == '__main__':
    unittest.main()
        



