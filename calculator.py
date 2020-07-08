def add(a, b):
    return (a+b)


def multiply(a, b):
    return (a*b)


def add_multiple(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


def multiply_multiple(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print(add_multiple(2, 4, 7, 5))
print(multiply_multiple(2, 6, 3))
