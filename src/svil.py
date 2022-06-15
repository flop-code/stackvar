from enum import Enum


class Commands(Enum):
    """
    This class (enum) is used to store all SVIL (Stackvar) commands.
    """

    PUSHSTACK = "pushstack"
    EXEC = "exec"
    GET = "get"
