from typing import Optional, Any
from stackvar import Exceptions as stvExceptions
from svil import Commands as svilCommands
import functions


stvFunctions = {
    k: v for k, v in functions.__dict__.items()
    if not k.startswith("__") and k.islower()
}


def stv_interpreter(parsed_code: list) -> int:
    """
    Stackvar interpreter.
    Accepts a list of SVIL lines (parsed_code) and executes it.
    Look in ../docs.txt for more information.
    """

    stack: list = []
    vars_: dict = {}

    for cmd, arg in parsed_code:
        if cmd == svilCommands.PUSHSTACK:
            stack.append(arg)
        elif cmd == svilCommands.GET:
            value: Any = vars_.get(arg)
            if value is not None:
                stack.append(value)
            else:
                print(f"Runtime error: Variable \"{arg}\" is not defined.")
                return 1
        elif cmd == svilCommands.EXEC:
            try:
                exception: Optional[stvExceptions] = stvFunctions[arg](stack, vars_)
                if exception is not None:
                    print(f"{exception.name}: {exception.value}")
                    return 1
            except Exception as e:
                print(f"Runtime error: {e}")
                return 1

    return 0
