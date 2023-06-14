def square(x: int | float) -> int | float:
    '''square function'''
    return x * x


def pow(x: int | float) -> int | float:
    '''pow function'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''outer function'''
    count = 0

    def inner() -> float:
        '''inner function'''
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner
