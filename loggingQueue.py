from multiprocessing import Process
import logging
"""
    Using super to inherit the process, for greater code organisation.
     
"""


class CustomLogging(Process):
    def __init__(self, queue):
        super(CustomLogging, self).__init__()
        self.queue = queue
        self.log = self.create_logger()

    def run(self):
        while True:  # need to exit at some stage+-
            record = self.queue.get()
            if record is None:
                print("closing")
                break
            else:
                self.handle(record)

    def create_logger(self):  # should probably be static. Just quick test
        """
        Creates a logging object and returns it
        """
        logger = logging.getLogger("example_logger")
        logger.setLevel(logging.INFO)

        # create the logging file handler
        fh = logging.FileHandler("test.log")

        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)
        return logger

    def handle(self, record):
        self.log.exception(record, exc_info=record)  # have to do better formatting here


