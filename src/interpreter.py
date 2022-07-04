from typing import Optional, Any, Union
from stackvar import Exceptions as stvExceptions
from svil import Commands as svilCommands
import functions


stvFunctions = {  # Connect all functions.
    k: v for k, v in functions.__dict__.items()
    if not k.startswith("_") and not k.endswith("_") and k.islower()
}

stvFunctions.update(functions.aliases_)  # Connect functions with aliases.


def _error(ind: int, cmd: svilCommands, arg: Any, msg: str) -> None:
    print(f"\nRuntime error on {ind} element (while {cmd} : \"{arg}\")\n{msg}")


def stv_interpreter(parsed_code: list,
                    _stack: Optional[list] = None,
                    _vars: Optional[dict] = None) -> Union[int, tuple]:
    """
    Stackvar interpreter.
    Accepts a list of SVIL lines (parsed_code) and executes it.
    Returns an exit code (1 if there are errors),
    or tuple with stack and variables lists, if there are no errors occurred.
    Look in ../docs.txt for more information.
    """

    if _stack is None:
        _stack = []
    if _vars is None:
        _vars = {}

    for ind, (cmd, arg) in enumerate(parsed_code, 1):
        if cmd == svilCommands.PUSHSTACK:
            _stack.append(arg)
        elif cmd == svilCommands.GET:
            value: Any = _vars.get(arg)
            if value is not None:
                _stack.append(value)
            else:
                _error(ind, cmd, arg, f"Unknown variable \"{arg}\"")
                return 1
        elif cmd == svilCommands.EXEC:
            if arg in functions.operators_:
                exception: Optional[stvExceptions] = functions.operator_(_stack, arg)
            else:
                try:
                    exception: Optional[stvExceptions] = stvFunctions[arg](_stack, _vars)
                except KeyError:
                    _error(ind, cmd, arg, f"Unknown function \"{arg}\".")
                    return 1
            if exception is not None:
                _error(ind, cmd, arg, f"{exception.name}: {exception.value}")
                return 1

    return _stack.copy(), _vars.copy()
