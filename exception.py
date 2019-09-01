class CustomHandling:
    """
    A decorator that wraps the passed in function. Will push exceptions to
    a queue.

    """

    def __init__(self, queue):
        self.attr = "a custom function attribute"
        self.queue = queue

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                # log the exception - Have to expand for more clarity
                err = "There was an exception in  "
                err += func.__name__
                self.queue.put(err)
                print(err)
        return wrapper

