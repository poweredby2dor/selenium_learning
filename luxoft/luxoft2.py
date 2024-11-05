#
# poweredby2dor
#
def function_1(b):
    return b + 5

def function_2(a, b):
    if b > 5:
        return function_1(a)
    else:
        return b

print(function_2(6, 7))
print(function_2(9, 3))