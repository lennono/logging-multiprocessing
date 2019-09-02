from multiprocessing import Process
"""
    Using super to inherit the process, for greater code organisation.
     
"""


class CustomLogging(Process):
    def __init__(self, queue):
        super(CustomLogging, self).__init__()
        self.queue = queue

    def run(self):
        while True:  # need to exit at some stage
            record = self.queue.get()
            if record is None:
                print("closing")
                break
            print(record)

