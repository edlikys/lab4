# счетчик вызовов функции
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(str(func.__name__) + " was called " + str(wrapper.count) + " times")
        return result
    wrapper.count = 0
    return wrapper


@counter
def give_me_sum(a, b):
    return a + b


print(give_me_sum(3, 2))
print(give_me_sum(3, 6))