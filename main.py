from utils.node import Node
from utils.bin_tree import arr_to_tree


lineList = list()
with open("./program.ze") as f:
    for line in f:
        lineList.append(line)

for operations in lineList:

    arr_operations = (
        operations.replace("(", "").replace(")", "").replace("\n", "").split(" ")
    )
    filter(None, arr_operations)

    tree, _ = arr_to_tree(arr_operations)

    tree.calc()
