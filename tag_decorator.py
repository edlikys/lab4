# параметризуемый декоратор для добавления тегов
def make_your_tag(tag):
    def wrapper(func):
        def decorate(*args, **kwargs):
            result = func(*args, **kwargs)
            return "<%s> %s </%s>" % (tag, str(result), tag)
        return decorate
    return wrapper


@make_your_tag("a")
@make_your_tag("i")
def hello():
    return "Hello!"


print(hello())
