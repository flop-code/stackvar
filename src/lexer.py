from stackvar import Types as stvTypes


SPECIAL_SIGNS = {
    "\\\\": "\\",
    "\\n": "\n",
    "\\r": "\r",
    '\\\"': '"'
}


def stv_lexer(code: str) -> list:
    """
    Stackvar code lexer.
    Accepts a string (code) and returns a list of pairs of tokens (see ../docs.txt).
    """

    if not code:
        return []

    code_lines: list = [
        line.split("#")[0].strip() for line in code.split('\n')
        if line.split("#")[0].strip()
    ]
    tokens: list = []
    skip_elems: int = 0
    elems: list = []
    string: str = ' '.join(code_lines)

    buff: str = ""
    skip_chars: int = 0
    depth_counter: int = 0
    for ind, char in enumerate(string):
        if skip_chars > 0:
            skip_chars -= 1
            continue
        if char == ' ':
            stripped_buff: str = buff.strip()
            if stripped_buff:
                if stripped_buff == "BEG":
                    stripped_buff = f"BEG_{depth_counter}"
                    depth_counter += 1
                elif stripped_buff == "END":
                    depth_counter -= 1
                    stripped_buff = f"END_{depth_counter}"
                elems.append(stripped_buff)
            buff = ""
        elif char in ('"', '('):
            end_char: str = ')' if char == '(' else '"'
            buff += char
            if buff[1:]:
                raise SyntaxError(f"Undefined literal \"{buff}\".")
            i: int = 1
            c: str = string[ind+i]
            try:
                while c != end_char:
                    buff += c
                    i += 1
                    c = string[ind+i]

                buff += end_char
                skip_chars = i
            except IndexError:
                raise SyntaxError(f"Unterminated string {buff}")
        elif char == '\\' and string[ind+1] == '"':
            buff += "\""
            skip_chars = 1
        else:
            buff += char
    else:
        elems.append(buff)

    for ind, elem in enumerate(elems):
        for k, v in SPECIAL_SIGNS.items():
            elem = elem.replace(k, v)
        if skip_elems > 0:
            skip_elems -= 1
            continue

        if elem == "TRUE" or elem == "FALSE":  # Boolean.
            tokens.append((stvTypes.BOOL, elem))
        elif elem.startswith('"'):  # String.
            tokens.append((stvTypes.STRING, elem[1:-1]))
        elif elem.startswith("("):  # Condition.
            condition: str = elem[1:-1]
            code_tokens: list = stv_lexer(condition)
            tokens.append((stvTypes.CONDITION, (code_tokens, condition)))
        elif elem.startswith('$'):  # Value of variable.
            tokens.append((stvTypes.VAR_VALUE, elem[1:]))
        elif elem.startswith('&'):  # Pointer to variable.
            tokens.append((stvTypes.VAR_POINTER, elem[1:]))
        elif elem.startswith('_'):  # Type.
            try:
                tokens.append((stvTypes[elem[1:]], None))
            except KeyError:
                raise SyntaxError(f"Unknown type: {elem}")
        elif elem.isdigit():        # Integer.
            tokens.append((stvTypes.INT, elem))
        elif elem.split("_")[0] == "BEG":  # Code.
            code: list = []
            depth: int = elem.split("_")[1]
            i: int = 1
            code_line: str = elems[ind+i]
            #print(ind, i, elems[ind+i], elems[32], elems[28])

            while code_line != f"END_{depth}":
                code.append(code_line)
                i += 1
                code_line = elems[ind+i]

            skip_elems = i
            code_tokens: list = stv_lexer(' '.join(code))
            tokens.append((stvTypes.CODE, code_tokens))
        else:  # Function.
            tokens.append((stvTypes.FUNCTION, elem))

    return tokens
