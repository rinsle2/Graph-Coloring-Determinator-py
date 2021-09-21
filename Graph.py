def make_graph():
    graph = Graph()
    return graph


class Graph:
    nodeCount = 0
    nodeMap = {}
    checks = []

    def __init__(self):
        self.nodeCount = 0
        self.nodeMap = {}
        self.checks = []
    
    def add_vertex(self, val):
        self.nodeMap[val] = []
        self.nodeCount += 1

    def add_edge(self, source, destination):
        if source in self.nodeMap:
            print("", end="")
        else:
            self.add_vertex(source)
        if destination in self.nodeMap:
            print("", end="")
        else:
            self.add_vertex(destination)
        self.nodeMap[source].append(destination)
        self.nodeMap[destination].append(source)

    def __populate(self):
        val = self.nodeCount
        for i in range(val):
            self.checks.append(True)
    # Swapping the >= for > is your initial state for this test, figure out what's wrong with this, find the pattern and fix it
    # Something is missing here, can you find what's missing? (I know what's missing, this is now everyone else's test)
    def __check_matrix(self, li: list, c):
        length = len(li)
        if (length == self.nodeCount - 1 or self.nodeCount > c) and length >= c:
            for i in range(len(self.checks)):
                if self.checks[i]:
                    self.checks[i] = False
                    break

    def __subset_true(self, c):
        full = 0
        for b in self.checks:
            if not b:
                full += 1
            if full > c:
                return True
        return False

    def is_colorable(self, c):
        self.__populate()
        for k in self.nodeMap:
            self.__check_matrix(self.nodeMap[k], c)
        return not self.__subset_true(c)
