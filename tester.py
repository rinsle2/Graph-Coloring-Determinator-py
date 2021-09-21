import unittest
import Graph as g


def petersonGraph(n: g):
    n.addEdge(1, 2)
    n.addEdge(1, 5)
    n.addEdge(1, 6)
    n.addEdge(2, 7)
    n.addEdge(2, 3)
    n.addEdge(3, 8)
    n.addEdge(3, 4)
    n.addEdge(4, 9)
    n.addEdge(4, 5)
    n.addEdge(5, 10)
    n.addEdge(6, 8)
    n.addEdge(6, 9)
    n.addEdge(8, 10)
    n.addEdge(10, 7)
    n.addEdge(7, 9)


def squareGraph(n: g):
    n.addEdge(1, 2)
    n.addEdge(2, 3)
    n.addEdge(3, 4)
    n.addEdge(4, 1)
    n.addEdge(4, 2)
    n.addEdge(1, 3)


class MyTestCase(unittest.TestCase):

    def test_square(self):
        n = g.Graph()
        squareGraph(n)
        self.assertEqual(n.isColorable(3), False)  # add assertion here

    def test_peterson(self):
        n = g.Graph()
        petersonGraph(n)
        self.assertEqual(n.isColorable(3), True)


if __name__ == '__main__':
    unittest.main()
