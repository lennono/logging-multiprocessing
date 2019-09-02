from functools import wraps


class CustomHandling:
    """
    A decorator that wraps the passed in function. Will push exceptions to
    a queue.

    """

    def __init__(self, queue):
        self.attr = "a custom function attribute"
        self.queue = queue

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:  # *Explained in two lines
                # log the exception - Have to expand for more clarity
                err = "There was an exception in "  # *need way better exceptions thrown
                err += func.__name__
                self.queue.put(err)
        return wrapper

