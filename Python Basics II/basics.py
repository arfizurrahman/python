# is_old = True
# is_licenced = True

# if is_old and is_licenced:
#     print("You'er old enough and licenced")
# elif is_licenced:
#     print('Licenced')
# else:
#     print("not old enough")

# ======== Ternary Operator

# Condition_if_true if condition else condition_if_false
# is_friend = True

# can_message = 'message allowed' if is_friend else 'message not allowed'

# print(can_message)

# =========== Short Circuting

is_friend = True
is_user = True

# ------------- is vs == ---------
# is compares references
# == compares value

# ========== For Loop =============
user = {
    'name': 'Arfiz',
    'age': 24,
    'is_cool': True
}

# for key, value in user.items():
#     print(value)

# for item in (1, 2, 3, 4, 5):
#     for x in ['a', 'b', 'c', 'd', 'e']:
#         print(f'{item} {x}')


# for number in range(1, 10):
#     print(number)

# ====== Enumerate
# for i, char in enumerate('hello'):
#     print(i, char)

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Arfiz')

while True:
    respose = input("Sat something")
    if(respose == "bye")
    break
