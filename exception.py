class CustomHandling:
    """
    A decorator that wraps the passed in function. Will push exceptions to
    a queue.

    """

    def __init__(self, queue):
        self.queue = queue

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (KeyboardInterrupt, SystemExit):
                pass
            except Exception as error:
                err = func.__name__
                self.queue.put((err, error))
                raise
        return wrapper

