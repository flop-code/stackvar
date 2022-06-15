from typing import Optional, Any, Union
from stackvar import Exceptions as stvExceptions, VariablePointer
from stackvar import Types as stvTypes

"""
Stackvar functions.

Each function accepts stack (and optional variables), and returns None or stvExceptions member.
(In my implementation stack is list, so function accepts reference to it)
functions returns None, if there is no error occurred, else it returns stvException
member.
"""


def print_(stack: list, vars_: Optional[dict] = None) -> Optional[stvExceptions]:
    try:
        print(stack.pop(-1)[1])
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def printn(stack: list, vars_: Optional[dict] = None) -> Optional[stvExceptions]:
    try:
        n: int = stack.pop(-1)
        if not isinstance(n, int):
            return stvExceptions.WrongTypeError
        for i in range(n):
            print(stack.pop(-1))
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def var(stack: list, vars_: Optional[dict] = None) -> Optional[stvExceptions]:
    try:
        name: str = stack.pop(-1)
        type_: stvTypes = stack.pop(-1)

        if not isinstance(name, str):
            return stvExceptions.WrongTypeError

        if type_ == stvTypes.INT:
            vars_[name[1]]: int = int()
        elif type_ == stvTypes.BOOL:
            vars_[name[1]]: bool = bool()
        elif type_ == stvTypes.STRING:
            vars_[name[1]]: str = str()
        else:
            return stvExceptions.UnknownTypeError

    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def push(stack: list, vars_: dict) -> Optional[stvExceptions]:
    try:
        pointer: VariablePointer = stack.pop(-1)
        value: Any = stack.pop(-1)
        var_type: Any = type(vars_[pointer.var_name])

        if not isinstance(value, var_type):
            return stvExceptions.WrongTypeError

        vars_[pointer.var_name] = value
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def add(stack: list, vars_: Optional[dict]) -> Optional[stvExceptions]:
    try:
        a: Union[int, str] = stack.pop(-1)
        b: Union[int, str] = stack.pop(-1)

        if not isinstance(a, (int, str)) or not isinstance(b, (int, str)):
            return stvExceptions.WrongTypeError

        stack.append(a + b)
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def sub(stack: list, vars_: Optional[dict]) -> Optional[stvExceptions]:
    try:
        a: int = stack.pop(-1)
        b: int = stack.pop(-1)

        if not isinstance(a, int) or not isinstance(b, int):
            return stvExceptions.WrongTypeError

        stack.append(a - b)
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def mul(stack: list, vars_: Optional[dict]) -> Optional[stvExceptions]:
    try:
        a: int = stack.pop(-1)
        b: int = stack.pop(-1)

        if not isinstance(a, int) or not isinstance(b, int):
            return stvExceptions.WrongTypeError

        stack.append(a * b)
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def div(stack: list, vars_: Optional[dict]) -> Optional[stvExceptions]:
    try:
        a: int = stack.pop(-1)
        b: int = stack.pop(-1)

        if not isinstance(a, int) or not isinstance(b, int):
            return stvExceptions.WrongTypeError

        stack.append(a // b)
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def mod(stack: list, vars_: Optional[dict]) -> Optional[stvExceptions]:
    try:
        a: int = stack.pop(-1)
        b: int = stack.pop(-1)

        if not isinstance(a, int) or not isinstance(b, int):
            return stvExceptions.WrongTypeError

        stack.append(a % b)
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def clear(stack: list, vars_: Optional[dict]) -> None:
    stack.clear()


def isempty(stack: list, vars_: Optional[dict]) -> None:
    if not stack:
        stack.append(True)
    else:
        stack.append(False)


def dup(stack: list, vars_: Optional[dict]) -> Optional[stvExceptions]:
    try:
        stack.append(stack[-1])
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError


def swap(stack: list, vars_: Optional[dict]) -> Optional[stvExceptions]:
    try:
        a: Any = stack.pop(-1)
        b: Any = stack.pop(-1)

        stack.append(a)
        stack.append(b)
    except IndexError:
        return stvExceptions.TakeFromEmptyStackError