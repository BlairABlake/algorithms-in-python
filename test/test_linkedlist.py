import unittest
from linkedlist import LinkedList


class TestObject: pass


class LinkedListTestCase(unittest.TestCase):
    def test_append_first(self):
        ll = LinkedList()
        obj = TestObject()

        ll.append(obj)

        self.assertEqual(id(ll.head.value), id(obj))

    def test_append(self):
        ll = LinkedList()
        objects = [TestObject() for i in range(10)]
        for obj in objects:
            ll.append(obj)

        for node, obj in zip(ll, objects):
            self.assertEqual(id(node.value), id(obj))

    def test_find(self):
        ll = LinkedList()
        objects = [TestObject() for i in range(10)]
        for obj in objects:
            ll.append(obj)

        target = objects[1]

        self.assertEqual(ll.find(target).value, target)

    def test_remove(self):
        ll = LinkedList()
        objects = [TestObject() for i in range(10)]
        for obj in objects:
            ll.append(obj)

        target = objects[1]
        wtarget = TestObject()

        self.assertEqual(ll.remove(target), 0)
        self.assertEqual(ll.remove(wtarget), -1)

if __name__ == '__main__':
    unittest.main()
