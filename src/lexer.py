from stackvar import Types as stvTypes


SPECIAL_SIGNS = {
    "\\\\": "\\",
    "\\n": "\n",
    "\\r": "\r",
    "\\\"": "\""
}


def parse_string(string: str) -> str:
    """
    Parses a string.
    """

    i: int = 1
    try:
        while string[i] != '"':
            if string[i] == '\\' and string[i + 1] == '"':
                i += 1
            i += 1
    except IndexError:
        raise SyntaxError(f"Unterminated string: {string}")

    parsed_string: str = string[1:i]

    # Replace special signs.
    for sign, repl in SPECIAL_SIGNS.items():
        parsed_string = parsed_string.replace(sign, repl)

    return parsed_string


def stv_lexer(code: str) -> list:
    """
    Stackvar code lexer.
    Accepts a string (code) and returns a list of pairs of tokens (see ../docs.txt).
    """

    code_lines: list = code.split('\n')
    tokens: list = []

    for line in code_lines:
        line: str = line.split('#')[0].strip()  # Remove comments.
        elems: list = line.split(";")
        if not elems:
            continue

        for ind, elem in enumerate(elems):
            elem = elem.strip()
            if not elem:
                continue

            if elem == "TRUE" or elem == "FALSE":  # Boolean.
                tokens.append((stvTypes.BOOL, elem))
            elif elem.startswith('"'):  # String.
                tokens.append((stvTypes.STRING, parse_string(elem)))
            elif elem.startswith('$'):  # Value of variable.
                tokens.append((stvTypes.VAR_VALUE, elem[1:]))
            elif elem.startswith('&'):  # Pointer to variable.
                tokens.append((stvTypes.VAR_POINTER, elem[1:]))
            elif elem.startswith('_'):  # Type.
                try:
                    tokens.append((stvTypes[elem[1:]], None))
                except KeyError:
                    raise SyntaxError(f"Unknown type: {elem}")
            elif elem.isdigit():  # Integer.
                tokens.append((stvTypes.INT, elem))
            else:  # Function.
                tokens.append((stvTypes.FUNCTION, elem))

    return tokens
