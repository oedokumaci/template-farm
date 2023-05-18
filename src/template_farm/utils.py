"""Module for utility functions."""

import logging
from time import time
from typing import Callable, ParamSpec, TypeVar

# Define TypeVars and ParamSpecs
R = TypeVar("R")
P = ParamSpec("P")


# Define a decorator function to print the execution time of a function
def timer_decorator(func: Callable[P, R]) -> Callable[P, R]:
    """Decorator that prints the time it took to execute a function.

    Args:
        func (Callable[P, R]): The function to be decorated.

    Returns:
        Callable[P, R]: The decorated function.
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        """Wrapper function that prints the time it took to execute a function.

        Args:
            *args (P.args): Positional arguments for the function.
            **kwargs (P.kwargs): Keyword arguments for the function.

        Returns:
            R: The result of the function.
        """
        # Get the start time and execute the function
        t1: float = time()
        result: R = func(*args, **kwargs)

        # Get the end time and calculate the elapsed time
        t2: float = time()
        elapsed_time = t2 - t1

        # Log the execution time and return the result of the function
        logging.info(
            f"Method {func.__name__!r} of module {func.__module__!r} executed in {elapsed_time:.4f} seconds"
        )
        return result

    return wrapper
