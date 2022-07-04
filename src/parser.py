from stackvar import Types as stvTypes,\
    VariablePointer as stvVariablePointer,\
    Code as stvCode,\
    Condition as stvCondition
from svil import Commands as svilCommands


def stv_parser(parsed_code: list) -> list:
    """
    Stackvar parser.
    Accepts a list of tokens (parsed_code) and returns SVIL list.
    Look in ../docs.txt for more information.
    """

    svil: list = []

    for pair in parsed_code:
        if pair[0] == stvTypes.STRING:
            if pair[1] is not None:
                svil.append((svilCommands.PUSHSTACK, pair[1]))
            else:
                svil.append((svilCommands.PUSHSTACK, stvTypes.STRING))
        elif pair[0] == stvTypes.INT:
            if pair[1] is not None:
                svil.append((svilCommands.PUSHSTACK, int(pair[1])))
            else:
                svil.append((svilCommands.PUSHSTACK, stvTypes.INT))
        elif pair[0] == stvTypes.BOOL:
            if pair[1] is not None:
                if pair[1] == "TRUE":
                    svil.append((svilCommands.PUSHSTACK, True))
                else:
                    svil.append((svilCommands.PUSHSTACK, False))
            else:
                svil.append((svilCommands.PUSHSTACK, stvTypes.BOOL))
        elif pair[0] == stvTypes.VAR_VALUE:
            svil.append((svilCommands.GET, pair[1]))
        elif pair[0] == stvTypes.VAR_POINTER:
            svil.append((svilCommands.PUSHSTACK, stvVariablePointer(pair[1])))
        elif pair[0] == stvTypes.FUNCTION:
            svil.append((svilCommands.EXEC, pair[1]))
        elif pair[0] == stvTypes.CODE:
            svil_code: list = stv_parser(pair[1])
            svil.append((svilCommands.PUSHSTACK, stvCode(svil_code)))
        elif pair[0] == stvTypes.CONDITION:
            svil_code: list = stv_parser(pair[1])
            svil.append((svilCommands.PUSHSTACK, stvCondition(svil_code)))

    return svil
