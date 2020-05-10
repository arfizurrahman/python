dictionary = {
    123: [1, 2, 3],
    'b': 2
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': 2
    },
    {
        'a': [4, 5, 6],
        'b': 2
    }
]

user = {
    'name': 'Arfiz',
    'age': 25
}

user2 = dict(name='Ashfaq')
print('age' in user)
print(user.get('age', 44))
print(user2)
