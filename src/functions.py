from typing import Optional, Any, Union
from stackvar import Exceptions as stvExceptions, \
    Types as stvTypes,\
    VariablePointer,\
    Code as stvCode,\
    Condition as stvCondition
import interpreter


"""
Stackvar functions.

Each function accepts stack (and optional variables), and returns None or stvExceptions member.
(In my implementation stack is list, so function accepts reference to it)
functions returns None, if there is no error occurred, else it returns stvException
member.
"""


def _get(stack: list, type_: Optional[Any] = None) -> tuple:
    """
    Get element from stack.
    Protected function.
    Is not a language command.
    Returns (True / False - Errors occured?, Value / stvException)
    """

    try:
        elem: Any = stack.pop(-1)
        if type_ is not None and not isinstance(elem, type_):
            return True, stvExceptions.WrongTypeError
        return False, elem
    except IndexError:
        return True, stvExceptions.TakeFromEmptyStackError


def _get_pair(stack: list, type1: Optional[Any] = None, type2: Optional[Any] = None) -> tuple:
    if type1 is None:
        r = _get(stack)
    else:
        r = _get(stack, type1)
    if r[0]:
        return True, (r[1], None)
    a: Any = r[1]

    if type2 is None:
        r = _get(stack)
    else:
        r = _get(stack, type2)

    if r[0]:
        return True, (r[1], None)
    b: Any = r[1]

    return False, (a, b)


def puts(stack: list, vars_: dict = None) -> Optional[stvExceptions]:
    r, elem = _get(stack)
    if r:
        return elem
    print(elem, end='')


def putsm(stack: list, vars_: dict = None) -> Optional[stvExceptions]:
    r, elem = _get(stack, int)
    if r:
        return elem

    n: int = elem
    for i in range(n-1):
        r, elem = _get(stack)
        if r:
            return elem
        print(elem, end=" ")
    else:
        r, elem = _get(stack)
        if r:
            return elem
        print(elem, end="")


def putsall(stack: list, vars_: dict) -> None:
    for i in range(len(stack)-1, 0, -1):
        print(stack[i], end=" ")
    else:
        print(stack[0], end="")


def var(stack: list, vars_: dict = None) -> Optional[stvExceptions]:
    r, (name, type_) = _get_pair(stack, str)

    if r:
        return name

    if type_ == stvTypes.INT:
        vars_[name]: int = int()
    elif type_ == stvTypes.BOOL:
        vars_[name]: bool = bool()
    elif type_ == stvTypes.STRING:
        vars_[name]: str = str()
    else:
        return stvExceptions.UnknownTypeError


def push(stack: list, vars_: dict) -> Optional[stvExceptions]:
    r, (pointer, value) = _get_pair(stack, VariablePointer)
    if r:
        return pointer
    vars_[pointer.var_name] = value


def operator_(stack, operator: str):
    r, (a, b) = _get_pair(stack, (int, str), (int, str))
    if r:
        return a

    try:
        if operator == '+':
            stack.append(a + b)
        elif operator == '-':
            stack.append(a - b)
        elif operator == '*':
            stack.append(a * b)
        elif operator == '/':
            stack.append(a / b)
        elif operator == '%':
            stack.append(a % b)
        elif operator == '**':
            stack.append(a ** b)
        elif operator == '&':
            stack.append(a & b)
        elif operator == '|':
            stack.append(a | b)
        elif operator == '^':
            stack.append(a ^ b)
        elif operator == '<<':
            stack.append(a << b)
        elif operator == '>>':
            stack.append(a >> b)
        elif operator == '=':
            stack.append(a == b)
        elif operator == "!=":
            stack.append(a != b)
        elif operator == '>':
            stack.append(a > b)
        elif operator == '<':
            stack.append(a < b)
        elif operator == '>=':
            stack.append(a >= b)
        elif operator == '<=':
            stack.append(a <= b)
    except TypeError:
        return stvExceptions.WrongTypeError


def clear(stack: list, vars_: dict) -> None:
    stack.clear()


def isempty(stack: list, vars_: dict) -> None:
    if not stack:
        stack.append(True)
    else:
        stack.append(False)


def dup(stack: list, vars_: dict) -> Optional[stvExceptions]:
    r, elem = _get(stack)
    if r:
        return elem

    stack.append(elem)


def swap(stack: list, vars_: dict) -> Optional[stvExceptions]:
    r, (a, b) = _get_pair(stack)
    if r:
        return a

    stack.extend((a, b))


def reverse(stack: list, vars_: dict) -> None:
    stack.reverse()


def cast(stack: list, vars_: dict) -> Optional[stvExceptions]:
    r, (type_, value) = _get_pair(stack)
    if r:
        return type_

    if type_ == stvTypes.INT:
        stack.append(int(value))
    elif type_ == stvTypes.BOOL:
        stack.append(bool(value))
    elif type_ == stvTypes.STRING:
        stack.append(str(value))
    else:
        return stvExceptions.UnknownTypeError


def read(stack: list, vars_: dict) -> None:
    stack.append(input())


def if_(stack: list, vars_: dict) -> Optional[stvExceptions]:
    r, (condition, code) = _get_pair(stack, bool, stvCode)
    if r:
        return condition

    if condition:
        exit_code: Optional[int, tuple] = interpreter.stv_interpreter(code.code, stack, vars_)
        if isinstance(exit_code, int):
            exit(exit_code)

        stack.clear()
        vars_.clear()
        stack.extend(exit_code[0])
        vars_.update(exit_code[1])


def ifelse(stack: list, vars_: dict) -> Optional[stvExceptions]:
    r, (condition, ifcode) = _get_pair(stack, bool, stvCode)
    if r:
        return condition

    r, elsecode = _get(stack, stvCode)
    if r:
        return ifcode

    if condition:
        code: stvCode = ifcode
    else:
        code: stvCode = elsecode

    exit_code: Optional[int, tuple] = interpreter.stv_interpreter(code.code, stack, vars_)
    if isinstance(exit_code, int):
        exit(exit_code)

    stack.clear()
    vars_.clear()
    stack.extend(exit_code[0])
    vars_.update(exit_code[1])


def _calculate_condition(condition: stvCondition) -> Union[bool, stvExceptions]:
    exit_code: Optional[int, tuple] = interpreter.stv_interpreter(condition.condition)
    if isinstance(exit_code, int):
        exit(exit_code)

    r, result = _get(exit_code[0], bool)
    if r:
        return result

    return result


aliases_: dict = {
    "if": if_,
    "while": while_
}

operators_: set = {
    "+", "-", "*", "/", "%", "**",
    "&", "|", "^", ">>", "<<",
    "=", "!=", ">", "<", ">=", "<="
}
