class Graph:
    nodeCount = 0
    nodeMap = {}
    checks = []

    def __init__(self):
        print("", end="")

    def addVertex(self, val):
        self.nodeMap[val] = []
        self.nodeCount += 1

    def addEdge(self, source, destination):
        if source in self.nodeMap:
            print("", end="")
        else:
            self.addVertex(source)
        if destination in self.nodeMap:
            print("", end="")
        else:
            self.addVertex(destination)
        self.nodeMap[source].append(destination)
        self.nodeMap[destination].append(source)

    def __populate(self):
        val = self.nodeCount
        for i in range(val):
            self.checks.append(True)

    # Something is missing here, can you find what's missing? (I know what's missing, this is now everyone else's test)
    def __checkMatrix(self, li: list, c):
        length = len(li)
        if (length == self.nodeCount - 1 or self.nodeCount > c) and length >= c:
            for i in range(len(self.checks)):
                if self.checks[i]:
                    self.checks[i] = False
                    break

    def __subsetTrue(self, c):
        full = 0
        for b in self.checks:
            if not b:
                full += 1
            if full > c:
                return True
        return False

    def isColorable(self, c):
        self.__populate()
        for k in self.nodeMap:
            self.__checkMatrix(self.nodeMap[k], c)
        print("Graph is ", end="")
        if self.__subsetTrue(c):
            print("not ", end="")
        print("fully colorable with {} colors".format(c), end="")
