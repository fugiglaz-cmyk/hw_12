from functools import wraps
from collections.abc import Callable
from typing import Any


def log_execution(func: Callable) -> Callable:
    """decorator for logging execution
    args: func: functions to log
    return: wrapper
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """wrapper for logging execution
        args: args and kwargs: any from func
        return: result
        """
        print(f"func started, {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"func ended, {func.__name__}({args}, {kwargs}), result: {result}")
        return result

    return wrapper


@log_execution
def say_hello(name: str) -> str:
    """func to say hello to somebody
    args: name: name
    return: str
    """
    return f'Hello {name}!'


print(say_hello('John'))
