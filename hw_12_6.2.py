import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def measure_time(func: Callable) -> Callable:
    """decorator for counting the time of operation
    args: func: the func we want to decorate
    return: wrapper
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """func wrapper
        args: args and kwargs: what given from the func
        return: result
        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("time:", end - start)
        return result

    return wrapper


@measure_time
def sum_numbers(*args: int | float) -> int | float:
    """func to calculate the sum of numbers
    args: the numbers
    return: sum of numbers
    """
    summa = 0
    for nums in args:
        summa += nums
    return summa


print(sum_numbers(1, 2, 3, 4, 5))
