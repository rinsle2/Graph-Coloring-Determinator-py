import unittest

import Graph


def square_graph(n):
    n.add_edge(1, 2)
    n.add_edge(2, 3)
    n.add_edge(3, 4)
    n.add_edge(4, 1)
    n.add_edge(4, 2)
    n.add_edge(1, 3)


def peterson_graph(n):
    n.add_edge(1, 2)
    n.add_edge(1, 5)
    n.add_edge(1, 6)
    n.add_edge(2, 7)
    n.add_edge(2, 3)
    n.add_edge(3, 8)
    n.add_edge(3, 4)
    n.add_edge(4, 9)
    n.add_edge(4, 5)
    n.add_edge(5, 10)
    n.add_edge(6, 8)
    n.add_edge(6, 9)
    n.add_edge(8, 10)
    n.add_edge(10, 7)
    n.add_edge(7, 9)


class MyTestCase(unittest.TestCase):

    def test_square(self):
        n = Graph.make_graph()
        square_graph(n)
        self.assertEqual(n.is_colorable(3), False)  # add assertion here
        del n

    def test_peterson(self):
        n = Graph.make_graph()
        peterson_graph(n)
        self.assertEqual(n.is_colorable(3), True)
        del n


if __name__ == '__main__':
    unittest.main()
