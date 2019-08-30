#  Timer and complicate data stractures


from functools import wraps
import time
import queue


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

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Linkedlist:
    def __init__(self, array=None):
        self.head = None
        self.size = 0

        if array:
            self.create_by_list(array)

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"<Linkedlist>: {self.head}"

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

    def reverse(self):

        prev = None
        head = self.head
        while head:
            temp = head.next
            head.next = prev

            prev = head
            head = temp
        self.head = prev

    def get_node(self, index):
        if index >= self.size:
            raise ValueError('Index out of range')

        last = self.head
        while index > 0:
            last = last.next
            index -= 1

        return last


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, array=None):
        self.root = None

        if array:
            self.create_by_list(array)

    def create_by_list(self, array):
        self.root = self._create(array, 0)
        pass

    def _create(self, array, index):
        if index >= len(array):
            return None

        if array[index] is None:
            return None

        node = TreeNode(array[index])
        node.left = self._create(array, 2*index + 1)
        node.right = self._create(array, 2*index + 2)

        return node

    def breadth_traversal(self):
        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            if node:
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                print(node.val)

    def depth_traversal(self):
        self._depth_traversal(self.root)

    def _depth_traversal(self, root):
        if not root:
            return
        print(root.val)
        self._depth_traversal(root.left)
        self._depth_traversal(root.right)
