# def hooo():
#     5/0

# hooo()

while True:
    try:
        age = int(input('Enter your age: '))
        10/age
        print(age)
        # raise ValueError('Cut it out')
        raise Exception('Cut it out')
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter a number higher than 0')
        break
    else:
        break
    finally:
        print("I'm finally done")
