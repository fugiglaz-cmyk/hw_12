from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def repeat(times: int) -> Callable:
    """func to repeat
    args: times: times to repeat
    return: repeat decorator
    """

    def repeat_decorator(func: Callable) -> Callable:
        """decorator to repeat
        args: func: func to repeat
        return: wrapper
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """wrapper
            args: args and kwargs: any from func
            return: result
            """
            for _ in range(times):
                try:
                    result = func(*args, **kwargs)
                except TypeError:
                    print("Attempt failed because of TypeError")
                    time.sleep(1)
                except ValueError:
                    print("Attempt failed because of ValueError")
                    time.sleep(1)
                except NameError:
                    print("Attempt failed because of NameError")
                    time.sleep(1)
                else:
                    return result

        return wrapper

    return repeat_decorator


@repeat(3)
def say_hello(name: str) -> str:
    """func to say hello to somebody
    args: name: name
    return: str
    """
    if not isinstance(name, str):
        raise TypeError
    return f'Hello {name}!'


print(say_hello("John"))
print(say_hello(1))
