# parameters
def say_hello(name='Farez', message='No Message'):
    print(f"Hello {name}, {message}")


# positional arguments
say_hello('Arfiz', 'How are you?')

# keyword arguments
say_hello(name='Arfiz', message='Ok!')


# def sum(num1, num2):
#     def another_function(n1, n2):
#         return n1 + n2
#     return another_function(num1, num2)


# print(sum(10, 20))


def test(a):
    '''
    Info: this function tests and printss param a 
    '''
    print(a)


help(test)
print(test.__doc__)


# *args and *kwargs

def super_func(*args, **kwargs):
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=6, num2=10))

# Rule: params, *args, default params, **kwargs

total = 0


def count(total):
    # global total
    total += 1
    return total


print(count(total))


# nonlocal
def outer():
    x = "local"
    typeo

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
