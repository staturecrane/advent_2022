import inspect
import os

import functools


def input_wrapper(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        directory = os.path.dirname(os.path.realpath(inspect.stack()[1].filename))

        with open(os.path.join(directory, "input.txt")) as f:
            lines = f.readlines()

        return func(lines, *args, **kwargs)

    return _wrapper
