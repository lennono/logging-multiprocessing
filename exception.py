def exception():
    """
    A decorator that wraps the passed in function. Will push exceptions to
    a queue.

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                # log the exception - Have to expand for more clarity
                err = "There was an exception in  "
                err += func.__name__
                # in a multi-processing example we would add to a queue.

            # re-raise the exception
            raise
        return wrapper
    return decorator
