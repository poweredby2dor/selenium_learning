# pylint: disable=missing-module-docstring
#
# poweredby2dor
#


# pylint: disable=missing-function-docstring
def function_1(b):
    return b + 5


# pylint: disable=no-else-return
def function_2(a, b):
    if b > 5:
        return function_1(a)
    else:
        return b

print(function_2(6, 7))
print(function_2(9, 3))
