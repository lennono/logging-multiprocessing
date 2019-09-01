from exception import CustomHandling
from multiprocessing import Queue
queue = Queue()


@CustomHandling(queue)
def zero_divide():
    1 / 0


if __name__ == '__main__':
    zero_divide()
