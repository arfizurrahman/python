# ============ Data types ============ #
# - [Fundamental data types]
# int
# float
# bool
# str
# list
# tuple
# set
# dict

# - [ User defined ]
# - [ Classes ]

# Specialized Data Types

# ============ Numbers ========= #
# print(type(2 + 4))
# print(2 - 4)
# print(2 / 4)
# print(6 // 4)
# print(2 ** 2)
# print(5 % 4)

# - [ math functions ]
# print(round(3.9))
# print(abs(-20))


# complex
# print(bin(5))
# print(int('0b101', 2))

# ============ Variables ============ #
# normal
# user_iq = 190
# private
# _iq = 200
# contants
# PI = 3.14

# print(user_iq)

# ============ Expressions vs statements ============ #
# iq = 130
# user_iq = iq / 5


# ============ string ============ #
# long_string = '''
# This
# is
# a
# long
# string
# '''
# print(long_string)
# ------ fomatted strings --------
# name = 'Arfiz'
# age = 25
# print(f'hi {name}. You are {age} years old')
# print('hi {}. You are {} years old'.format(name, age))

# ------ string indexes ------
# [start:stop:stepover]
# selfish = '0123457'
# print(selfish[0:5:2])
# print(selfish[0:])
# print(selfish[:5])
# print(selfish[::2])
# print(selfish[-1])  # from the end
# print(selfish[::-1])  # reverse

# ========== Built in functions =========
# print(len('hellooooo'))

name = input('name: ')
password = input('secret: ')
password_length = len(password)
hidden_password = '*' * password_length
print(f'Hey {name}, your password {hidden_password} is {password_length} characters long')
