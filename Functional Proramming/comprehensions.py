# list, set, dictionary
my_list = [char for char in 'hello']
my_list2 = [number for number in range(0, 100)]
my_list3 = [number*2 for number in range(0, 100)]
my_list4 = [number**2 for number in range(0, 100) if number % 2 == 0]

# for char in 'hello':
#     my_list.append(char)

my_set = {char for char in 'hello'}
my_set2 = {number for number in range(0, 100)}
my_set3 = {number*2 for number in range(0, 100)}
my_set4 = {number**2 for number in range(0, 100) if number % 2 == 0}

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}
my_dict2 = {key: key*2 for key in [1, 2, 3]}
print(my_dict2)
