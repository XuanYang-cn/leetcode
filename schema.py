#  Timer and complicate data stractures


from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def inner(*args):
        date = ('{}-{}-{} {}:{}:{}').format(*time.localtime(time.time()))
        t0 = time.perf_counter_ns()
        _result = func(*args)
        elapsed = (time.perf_counter_ns() - t0)/1000
        if _result is not None:
            print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__} -> {_result}')
        else:
            print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__}')
        return _result
    return inner


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        head = self.head
        result = ''
        while head:
            result += str(head.val) + ' -'
            head = head.next
        return result

    def create_by_list(self, array):
        temp = self.head
        for item in array:
            if not temp:
                temp = Node(item)
                self.head = temp
            else:
                temp.next = Node(item)
                temp = temp.next
            self.size += 1

    def append(self, x):
        head = self.head
        if not head:
            head = Node(x)
        else:
            head.next = Node(x)
        self.size += 1
