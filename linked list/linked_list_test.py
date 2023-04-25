import unittest
import sys
import io

from linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList(Node(1))

    def test_insert(self):
        self.list.insert(2)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.head.data, 2)
        self.assertEqual(self.list.head.next.data, 1)

    def test_append(self):
        self.list.append(2)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.head.next.data, 2)
        self.assertEqual(self.list.head.next.next, None)

    def test_find(self):
        self.assertFalse(self.list.find(2))
        self.assertTrue(self.list.find(1))

    def test_delete(self):
        self.list.delete(1)
        self.assertEqual(len(self.list), 0)
        self.assertEqual(self.list.head, None)

    def test_get_all_data(self):
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.get_all_data(), "1 => 2 => 3")

    def test_print_list(self):
        self.list.append(2)
        self.list.append(3)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.list.print_list()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1\n2\n3")


if __name__ == '__main__':
    unittest.main()
