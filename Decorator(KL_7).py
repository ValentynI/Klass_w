def checker(function):
    def checker_1(*args, **kwards):
        try:
            result = function(*args, **kwards)
        except Exception as exc:
            print(f'We have problems {exc}')
        else:
            print(result)
    return checker_1


def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
calculate('2+2')