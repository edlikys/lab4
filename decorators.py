from datetime import datetime


def some_decorator(num):
    def wrapper(func):
        def tmp(*args, **kwargs):
            result = func(*args, **kwargs) * num
            return result
        return tmp
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@timer
@some_decorator(3)
def my_func(a, b):
    return a+b

@timer
@some_decorator(4)
def another_func():
    return "Lalala\n"


print(my_func(3, 2))
print(another_func())