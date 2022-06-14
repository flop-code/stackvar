from enum import Enum


class Types(Enum):
    """
    This class (enum) is used to store all Stackvar types.
    """

    INT = "int"
    BOOL = "bool"
    STRING = "string"
    LL = "long long"
    ULL = "unsigned long long"
    UINT = "unsigned int"
    VAR_POINTER = "&"
    VAR_VALUE = "$"
    FUNCTION = "f"
