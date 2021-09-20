# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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


def main():
    n = g.Graph()
    # squareGraph(n)
    petersonGraph(n)
    n.isColorable(3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
