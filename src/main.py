from sys import argv

from parser import stv_parser
from lexer import stv_lexer
from interpreter import stv_interpreter


DEV_MODE: bool = False


def main(args: list) -> None:
    global DEV_MODE
    filename: str = args[0]
    with open(filename, 'r') as f:
        code = f.read()

    DEV_MODE = "--dev" in args

    parsed_code = stv_parser(code)
    errors = stv_lexer(parsed_code)
    if errors:
        exit(1)

    stv_interpreter(parsed_code)


if __name__ == "__main__":
    main(argv[1:])
