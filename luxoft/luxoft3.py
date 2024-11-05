#
# poweredby2dor
#

def func_1(a):
    i = 0
    while i < 3:
        a = a + 2
        i = i + 1
    if True:
        a = 10
    else:
        a = 100
    return a

result = func_1(20)
print("The result for func_1 is: ", result)
print(f"func_1 will always return 10 because of the if True condition")