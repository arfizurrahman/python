# Pure fuctions
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list


from functools import reduce


def multiply_by2(item):
    return item * 2


# map()
# print(list(map(multiply_by2, [1, 2, 3])))

# print(multiply_by2([1, 2, 3]))

def odd(item):
    return item % 2 != 0


my_list = [1, 2, 3]
your_list = [10, 20, 30]
your_list1 = [10, 20, 30]
# filter()
# print(list(filter(odd, [1, 2, 3])))
# print(list(zip(my_list, your_list, your_list1)))

# reduce()


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
