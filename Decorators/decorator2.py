def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func


@my_decorator
def hello(greeting, em):
    print(greeting, em)


hello('hiii', ':)')


@my_decorator
def bye():
    print('See ya')


# hello2 = my_decorator(hello)
# hello2()
