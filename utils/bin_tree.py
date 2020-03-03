from utils.runtime import operators


def arr_to_tree(arr):
    from utils.node import Node

    if arr[0] not in operators:
        return Node(arr[0]), arr[1:]

    tmp = Node(arr[0])
    op = arr[0]
    arr = arr[1:]

    for _ in range(operators[op]["arg_len"]):
        tmpNode, arr = arr_to_tree(arr)
        tmp.nodes.append(tmpNode)

    return tmp, arr
