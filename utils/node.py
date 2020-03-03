class Node:
    def __init__(self, data):
        self.data = data
        self.nodes = []

    def PrintTree(self):
        print(self.data)

    def calc(self):
        from utils.bin_tree import operators

        if self.data in operators:
            return operators[self.data]["fn"](
                list(map(lambda node: node.calc(), self.nodes))
            )

        return self.data
