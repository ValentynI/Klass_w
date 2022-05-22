try:
    print('----')
    print('----')
    print('----')
    print('----')
    print(10/0)
    print('----')
    my_list = []
    print(my_list[3])
except BaseException as error:
    print(type(error).__name__+": "+str(error))

else:
    print('Ok')

print('Hello!')

print('------------------------------')


def checker(x):
    if type(x) != int:
        raise TypeError('Please, we need INT')
a = 'dog'
try:
    checker(a)
except TypeError:
    print('ERROR')