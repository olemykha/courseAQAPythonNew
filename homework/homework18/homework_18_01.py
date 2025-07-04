from functools import wraps

# generators:


def even_numbers(n: int):

    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def fibonacci(n: int):

    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# iterators:


class ReverseIterator:

    def __init__(self, data_list: list):
        self._data = data_list
        self._index = len(data_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._data[self._index]


class EvenIterator:

    def __init__(self, n: int):
        self._n = n
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self._n:
            raise StopIteration
        value = self._current
        self._current += 2
        return value

# decorators:


def log_calls(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result!r}")
        return result
    return wrapper


def catch_exceptions(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Exception in {func.__name__}: {e}")
            return None
    return wrapper
