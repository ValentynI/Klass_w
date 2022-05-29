def raise_to_the_degrees(number):
    i = 0
    while True:
        yield number**i
        i += 1
res = raise_to_the_degrees(12)
print(res)
for _ in range(100):
    print(next(res))

print('-------------------------------')
def raise_to_the_degrees(number):
    i = 0
    while True:
        result = number**i
        yield result
        if result > 10**20:
            return
        i += 1
res = raise_to_the_degrees(12)
print(res)
for _ in res:
    print(_)