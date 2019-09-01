class CustomLogging:
    def __init__(self, queue):
        self.queue = queue

    def log_error(self):
        while True:
            print(self.queue.get())


