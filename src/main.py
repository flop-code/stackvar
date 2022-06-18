from sys import argv

from lexer import stv_lexer
from parser import stv_parser
from interpreter import stv_interpreter


DEV_MODE: bool = False


def interactive_mode():
    while True:
        try:
            code: str = ""
            print("New program:")
            u_input: str = input("> ")
            while u_input != "#end":
                code += u_input + "\n"
                u_input = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        stv_interpreter(stv_parser(stv_lexer(code)))
        print("\nEnd of program.")


def main(args: list) -> None:
    global DEV_MODE

    if DEV_MODE:
        filename: str = "test.stv"
    else:
        try:
            filename: str = args[0]
        except IndexError:
            print("Stackvar language interactive mode.")
            print("Write \"end\" to finish your program.")
            interactive_mode()
            return

    with open(filename, 'r') as f:
        code = f.read()

    tokens: list = stv_lexer(code)
    svil: list = stv_parser(tokens)

    if "--dev" in args or DEV_MODE:
        print("Tokens:")
        print(tokens)
        print("\n\nSVIL:")
        print(svil)
        print()

    exit(stv_interpreter(svil))


if __name__ == "__main__":
    main(argv[1:])
