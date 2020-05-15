try:
    with open('app/tet2.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
except FileNotFoundError as err:
    print('File doesn\'t exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
