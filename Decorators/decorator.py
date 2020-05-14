def hello():
    print('hello')


greet = hello
del hello

greet()
