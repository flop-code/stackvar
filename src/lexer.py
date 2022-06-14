from StackvarTypes import Types


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

    string = string[1:i]

    # Replace special signs.
    for sign, repl in SPECIAL_SIGNS.items():
        string = string.replace(sign, repl)

    return string


def stv_lexer(code: str) -> list:
    """
    Stackvar code lexer.
    Accepts a string (code) and returns a list of tokens (see ../docs.txt).
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

            if elem.startswith('"'):  # String.
                tokens.append({Types.STRING: parse_string(elem)})
            elif elem.startswith('$'):  # Value of variable.
                tokens.append({Types.VAR_VALUE: elem[1:]})
            elif elem.startswith('&'):  # Pointer to variable.
                tokens.append({Types.VAR_POINTER: elem[1:]})
            elif elem.startswith('_'):  # Type.
                try:
                    tokens.append({Types[elem[1:]]: None})
                except KeyError:
                    raise SyntaxError(f"Unknown type: {elem}")
            elif elem.isdigit():  # Integer.
                tokens.append({Types.INT: elem})
            else:  # Function.
                tokens.append({Types.FUNCTION: elem})

    return tokens
