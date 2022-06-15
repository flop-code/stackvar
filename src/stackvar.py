from enum import Enum
from dataclasses import dataclass


@dataclass
class VariablePointer:
    """
    This class (struct) is used to store the "pointer" to a variable.
    """

    var_name: str


class Types(Enum):
    """
    This class (enum) is used to store all Stackvar types.
    """

    INT = "int"
    BOOL = "bool"
    STRING = "string"
    VAR_POINTER = "&"
    VAR_VALUE = "$"
    FUNCTION = "f"


class Exceptions(Enum):
    """
    This class (enum) is used to store Stackvar runtime exceptions.
    """

    TakeFromEmptyStackError = "Getting element from empty stack"
    UnknownVariableError = "Accessing to undefined variable"
    UnknownFunctionError = "Accessing to undefined function"
    UnknownTypeError = "Accessing to unknown type"
    WrongTypeError = "Using wrong type"
    InternalError = "Unknown error while execution"
