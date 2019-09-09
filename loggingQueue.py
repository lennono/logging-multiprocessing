from multiprocessing import Process
import logging
"""
    Using super to inherit process, for greater code organisation.
     
"""


class CustomLogging(Process):
    def __init__(self, queue):
        super(CustomLogging, self).__init__()
        self.queue = queue
        self._log = None

    def run(self):
        while True:
            record = self.queue.get()
            if record is None:
                break
            print(record)

    @property
    def create_logger(self, record):  # should probably be static. Just quick test
        """
        Creates a logging object and logs error
        """
        logger = logging.getLogger(record[0])
        logger.setLevel(logging.DEBUG)

        # create the logging file handler
        fh = logging.FileHandler("logs/logs.log")

        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)
        logger.exception(record[0], exc_info=record[1])
        return self._log


