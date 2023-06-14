def ft_mean(lst: list):
    '''mean function'''
    if len(lst) == 0:
        return "ERROR"
    res = 0
    for i in lst:
        res += i

    return res / len(lst)


def ft_median(lst: list):
    '''median function'''
    if len(lst) == 0:
        return "ERROR"
    lst.sort()
    n = len(lst)

    return (lst[n//2-1]/2.0+lst[n//2]/2.0, lst[n//2])[n % 2] if n else None


def ft_quartile(lst: list):
    '''quartile function'''
    if len(lst) == 0:
        return "ERROR"
    lst.sort()
    n = len(lst)
    first = lst[int(0.25 * n)]
    third = lst[int(0.75 * n)]
    return float(first), float(third)


def ft_var(lst: list):
    '''var function'''
    if len(lst) == 0:
        return "ERROR"
    lst.sort()
    n = len(lst)
    mean = sum(lst) / n
    dev = [(x - mean) ** 2 for x in lst]
    return sum(dev) / n


def ft_std(lst: list):
    '''std function'''
    if len(lst) == 0:
        return "ERROR"
    lst.sort()

    return ft_var(lst) ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''stat function'''
    nlist = list(args)
    assert all(isinstance(n, int) for n in nlist), "ERROR"

    values = [value for key, value in kwargs.items()]

    for i in values:
        match i:
            case "median":
                print(ft_median(nlist))
            case "mean":
                print(ft_mean(nlist))
            case "quartile":
                print(ft_quartile(nlist))
            case "std":
                print(ft_std(nlist))
            case "var":
                print(ft_var(nlist))
