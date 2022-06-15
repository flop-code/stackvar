from sys import argv

from lexer import stv_lexer
from parser import stv_parser
from interpreter import stv_interpreter


DEV_MODE: bool = False


def main(args: list) -> None:
    global DEV_MODE

    filename: str = args[0]
    with open(filename, 'r') as f:
        code = f.read()

    DEV_MODE = "--dev" in args

    tokens: list = stv_lexer(code)
    svil: list = stv_parser(tokens)

    if DEV_MODE:
        print(tokens)
        print("\n--------- SVIL ---------\n")
        print(svil)

    stv_interpreter(svil)


if __name__ == "__main__":
    main(argv[1:])
