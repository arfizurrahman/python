# debugging

# linting
# ide/editor
# read errrors
# pdb

import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, 4)
