# lambda param: action(param)
from functools import reduce
my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

a = [(12, -2), (4, 3), (9, 9), (10, -1)]
sorted = []
# print(list(map(lambda item: expression)))

a.sort(key=lambda item: item[1])
print(a)
