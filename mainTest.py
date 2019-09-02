from exception import CustomHandling
from loggingQueue import CustomLogging
from multiprocessing import Queue
queue = Queue()  # Need  a better solution here


@CustomHandling(queue)
def zero_divide():
    1 / 0  # throwing deliberate error


if __name__ == '__main__':
    p = CustomLogging(queue)
    p.start()
    zero_divide()
    queue.put(None)

