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
            try:  # will keep expanding
                return func(*args, **kwargs)
            except ValueError as error:
                print(error)
            except (TypeError, ZeroDivisionError) as error:
                err = "There was an exception in "
                err += func.__name__
                self.queue.put(error)
            except:
                pass
        return wrapper

