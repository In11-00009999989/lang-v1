def read_file(args):
    with open(args[0], "r") as f:
        print(f.read())


operators = {
    "+": {"arg_len": 2, "fn": lambda args: int(args[0]) + int(args[1])},
    "-": {"arg_len": 2, "fn": lambda args: int(args[0]) - int(args[1])},
    "*": {"arg_len": 2, "fn": lambda args: int(args[0]) * int(args[1])},
    "/": {"arg_len": 2, "fn": lambda args: int(args[0]) / int(args[1])},
    "$": {"arg_len": 1, "fn": lambda args: int(args[0]) ** 2},
    "#": {"arg_len": 1, "fn": lambda args: int(args[0]) ** 3},
    "log": {"arg_len": 1, "fn": lambda args: print(args[0])},
    "read_file": {"arg_len": 1, "fn": read_file},
}
